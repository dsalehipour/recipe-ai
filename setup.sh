#!/bin/bash

echo "🍳 Recipe AI Setup Script"
echo "========================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or later."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip3."
    exit 1
fi

echo "✅ Python and pip found"
echo "📦 Installing dependencies..."

# Install requirements
pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully!"
    echo ""
    echo "🔑 Next steps:"
    echo "1. Get your OpenAI API key from: https://platform.openai.com/api-keys"
    echo "2. Create a .env file with your API key:"
    echo "   echo 'OPENAI_API_KEY=your_actual_api_key_here' > .env"
    echo ""
    echo "🚀 Then run the app with:"
    echo "   python3 run.py"
    echo "   or"
    echo "   python3 app.py"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi 