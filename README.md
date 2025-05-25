# 🍳 Recipe AI Web App

A simple, beautiful web application that generates custom recipes using OpenAI's GPT model and finds related YouTube cooking videos. Just type what you want to cook, and get detailed ingredients, step-by-step instructions, and 3 helpful cooking videos!

## Features

- ✨ Clean, modern UI with responsive design
- 🤖 Powered by OpenAI GPT-3.5-turbo
- 🎥 **NEW**: 3 related YouTube cooking videos for each recipe
- 📱 Mobile-friendly interface
- ⚡ Real-time recipe generation
- 🍽️ Detailed ingredients and cooking instructions
- ⏱️ Cooking time and serving estimates
- 🎬 Embedded video player modal

## Screenshot

The app features a beautiful gradient background with a clean white card interface, example recipe buttons, formatted recipe output, and a video gallery with embedded YouTube tutorials.

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set up API Keys

#### OpenAI API Key
1. Get your OpenAI API key from [OpenAI Platform](https://platform.openai.com/api-keys)

#### Environment File
Create a `.env` file in the project root:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

Replace the placeholder with your actual OpenAI API key.

**Note**: YouTube videos are now fetched without requiring a YouTube API key!

### 3. Run the Application

```bash
python app.py
```

The app will start on `http://localhost:3000`

## Usage

1. Open your browser and go to `http://localhost:3000`
2. Type any recipe request in the input field, such as:
   - "chicken tikka masala"
   - "chocolate chip cookies"
   - "vegetarian pasta"
   - "homemade pizza"
3. Toggle "Make from scratch" if you want everything made from basic ingredients
4. Click "Get Recipe" or press Enter
5. Wait a few seconds for the AI to generate your custom recipe
6. **NEW**: Browse the 3 YouTube cooking videos below the recipe
7. Click on any video thumbnail or "Watch Tutorial" to play the video
8. Enjoy cooking with both written instructions and video guidance!

## Example Requests

- **Simple**: "pasta", "cookies", "soup"
- **Specific**: "spicy Thai green curry", "New York style cheesecake"
- **Dietary**: "vegan chocolate brownies", "gluten-free bread"
- **Cuisine**: "authentic Italian carbonara", "Japanese ramen"

## Project Structure

```
recipe-ai/
├── app.py              # Flask backend application
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── env_example.txt    # Example environment variables
└── templates/
    └── index.html     # Frontend HTML template
```

## Technical Details

- **Backend**: Python Flask
- **Frontend**: HTML, CSS, JavaScript
- **AI Model**: OpenAI GPT-3.5-turbo
- **Video Search**: youtube-search-python (no API key required)
- **Styling**: Custom CSS with gradient backgrounds and animations

## API Endpoints

- `GET /` - Serves the main page
- `POST /get_recipe` - Generates recipe from user input and fetches related YouTube videos

## Error Handling

The app includes comprehensive error handling for:
- Missing API keys
- Invalid requests
- Network issues
- OpenAI API errors
- YouTube API errors

## Customization

You can easily customize:
- **Model**: Change `gpt-3.5-turbo` to `gpt-4` in `app.py` for better quality (higher cost)
- **Video Count**: Modify `max_results=3` in the `search_youtube_videos` function
- **Styling**: Modify the CSS in `templates/index.html`
- **Prompt**: Adjust the recipe generation prompt in `app.py`
- **Examples**: Add more example recipes in the HTML

## Cost Considerations

This app uses OpenAI's API:
- **OpenAI**: GPT-3.5-turbo is very affordable, typically costing less than $0.01 per recipe
- **YouTube Videos**: Free! No API key or quota limits required

## License

MIT License - feel free to use and modify as needed!

---

Built with ❤️ for food lovers and cooking enthusiasts! # recipe-ai
