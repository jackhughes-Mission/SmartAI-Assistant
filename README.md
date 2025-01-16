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
- If your python version doesn't work, use 3.11. I created a virtual environment with 3.11.

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

## Usage
Run the program using:
```bash
python main.py
```

## Acknowledgments
- OpenAI for providing the API.
- EdgeTTS for providing the TTS functionality.
- Bleak for providing the BLE functionality.
- SpeechRecognition for providing the STT functionality.
- Pyttsx3 for providing the TTS functionality.
- PyAudio for providing the audio functionality.
- Pytz for providing the time functionality.
- dotenv for providing the environment variables.