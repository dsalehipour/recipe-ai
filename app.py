from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os
from dotenv import load_dotenv
from youtubesearchpython import VideosSearch

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def search_youtube_videos(recipe_name, from_scratch=False, max_results=3):
    """Search for cooking videos on YouTube related to the recipe"""
    try:
        # Create a search query for cooking videos
        if from_scratch:
            search_query = f"{recipe_name} recipe from scratch homemade tutorial"
        else:
            search_query = f"{recipe_name} recipe cooking tutorial"
        
        # Search for videos
        videos_search = VideosSearch(search_query, limit=max_results)
        results = videos_search.result()
        
        videos = []
        for video_data in results['result']:
            video_id = video_data['id']
            video_title = video_data['title']
            video_thumbnail = video_data['thumbnails'][0]['url'] if video_data['thumbnails'] else ''
            channel_title = video_data['channel']['name']
            duration = video_data.get('duration', 'N/A')
            view_count = video_data.get('viewCount', {}).get('text', 'N/A')
            
            videos.append({
                'id': video_id,
                'title': video_title,
                'thumbnail': video_thumbnail,
                'channel': channel_title,
                'duration': duration,
                'views': view_count,
                'url': f"https://www.youtube.com/watch?v={video_id}",
                'embed_url': f"https://www.youtube.com/embed/{video_id}"
            })
        
        return videos
    except Exception as e:
        print(f"Error fetching YouTube videos: {str(e)}")
        return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_recipe', methods=['POST'])
def get_recipe():
    try:
        data = request.get_json()
        recipe_request = data.get('recipe_request', '')
        from_scratch = data.get('from_scratch', False)
        
        if not recipe_request:
            return jsonify({'error': 'Please provide a recipe request'}), 400
        
        # Create a prompt for OpenAI
        base_prompt = f"""
        Please provide a detailed recipe for: {recipe_request}
        """
        
        if from_scratch:
            base_prompt += """
        
        CRITICAL REQUIREMENT - MAKE EVERYTHING FROM SCRATCH: 
        This recipe must be made completely from scratch using only basic, raw ingredients. You MUST include detailed instructions for making ALL components from basic ingredients. Do NOT list any pre-made, processed, or store-bought items as ingredients.

        Examples of what must be made from scratch:
        - ANY pastry or dough (puff pastry, pie crust, pasta dough, bread dough, pizza dough, etc.) - provide full recipes starting from flour, butter, eggs, etc.
        - ALL sauces and condiments (stocks, broths, tomato sauce, mayonnaise, mustard, etc.) - make from basic ingredients
        - ANY baked goods components (cookies, crackers, breadcrumbs, etc.)
        - Dairy products if possible (butter from cream, cheese from milk, etc.)
        - Spice blends and seasoning mixes
        - ANY processed ingredients - if the recipe calls for something that comes in a package, make it from scratch instead

        For each component that would normally be store-bought, provide:
        1. Complete ingredient list for that component
        2. Step-by-step instructions for making it
        3. Integration into the main recipe timeline

        Start with the most time-consuming components first and work efficiently.
        """
        
        base_prompt += """
        Format your response as follows:
        RECIPE NAME: [Name of the dish]
        
        INGREDIENTS:
        - [ingredient 1]
        - [ingredient 2]
        - [etc.]
        
        INSTRUCTIONS:
        1. [step 1]
        2. [step 2]
        3. [etc.]
        
        COOKING TIME: [estimated time]
        SERVINGS: [number of servings]
        """
        
        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful cooking assistant that provides clear, detailed recipes."},
                {"role": "user", "content": base_prompt}
            ],
            max_tokens=2500,
            temperature=0.7
        )
        
        recipe = response.choices[0].message.content
        
        # Search for YouTube videos related to the recipe
        videos = search_youtube_videos(recipe_request, from_scratch)
        
        return jsonify({
            'recipe': recipe,
            'videos': videos
        })
        
    except Exception as e:
        return jsonify({'error': f'Error generating recipe: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000) 