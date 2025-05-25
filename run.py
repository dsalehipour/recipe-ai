#!/usr/bin/env python3
"""
Recipe AI Web App Runner
Simple startup script with helpful error messages
"""

import os
import sys
from dotenv import load_dotenv

def check_requirements():
    """Check if all requirements are met before starting the app"""
    
    # Load environment variables
    load_dotenv()
    
    # Check if OpenAI API key is set
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ Error: OpenAI API key not found!")
        print("\n📝 Please follow these steps:")
        print("1. Get your API key from: https://platform.openai.com/api-keys")
        print("2. Create a .env file in this directory")
        print("3. Add this line to the .env file:")
        print("   OPENAI_API_KEY=your_actual_api_key_here")
        print("\n💡 You can also set it temporarily with:")
        print("   export OPENAI_API_KEY=your_actual_api_key_here")
        return False
    
    # Check if required packages are installed
    try:
        import flask
        import openai
    except ImportError as e:
        print(f"❌ Error: Missing required package: {e}")
        print("\n📦 Please install requirements:")
        print("   pip install -r requirements.txt")
        return False
    
    return True

def main():
    """Main function to run the app"""
    
    print("🍳 Recipe AI Web App")
    print("=" * 30)
    
    if not check_requirements():
        sys.exit(1)
    
    print("✅ All requirements met!")
    print("🚀 Starting the Recipe AI web app...")
    print("📱 Open your browser and go to: http://localhost:3000")
    print("🛑 Press Ctrl+C to stop the server")
    print("\n" + "=" * 50 + "\n")
    
    # Import and run the app
    from app import app
    app.run(debug=True, port=3000, host='0.0.0.0')

if __name__ == '__main__':
    main() 