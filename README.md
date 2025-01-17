# Smart Home Assistant

## Overview
The Smart Home Assistant is a smart program that utilises the OpenAI API along with Text-to-Speech (TTS) and Speech-to-Text (STT) technologies. It interprets user input and generates responses, allowing for interactive conversations.

## Features
- **Conversational AI**: Engage in natural conversations with the assistant.
- **Smart Device Control**: Control various smart devices around your home.
- **Information Retrieval**: Get basic information such as the weather and time.

## Prerequisites
To run this project, ensure you have the following installed:
- Python 3.x
- Required packages (install via `pip install -r requirements.txt`)
- If your python version doesn't work, use 3.11.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd SmartGPT-RaspPi-Assistant
   ```
3. Set up a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
5. Add your OpenAI API key to the .env file.
   ```bash
   OPENAI_API_KEY=your_api_key
   ```

## Usage
Run the program using:
```bash
python main.py
```

## Requirements in detail
- OpenAI for providing the chatgpt conversation functionality.
- EdgeTTS for providing the real sounding TTS.
- Bleak for providing the bluetooth scanning and control.
- SpeechRecognition for providing the STT.
- Pygame for providing the audio functionality.
- Pytz for providing access to the time.
- Dotenv for providing the environment variables.
- Asyncio for providing the async functionality.
- Pyvesync for providing access to the air purifier.
- Keyring for providing password storage.
- Fuzzywuzzy for providing the fuzzy matching functionality.