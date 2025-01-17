from dotenv import load_dotenv
import os
from openai import OpenAI
import speech_recognition as sr
import pygame
import asyncio
import edge_tts

from air_purifier import main_purifier, turn_on, turn_off, high_purifier, low_purifier
from basic_func import get_country
from intents import INTENTS_LIST, INSTRUCTIONS

from led_lamp import asyncio_turnon, asyncio_turnoff, connect_sync

VOICE = "en-GB-SoniaNeural"
OUTPUT_FILE = "temp-speech.mp3"

def load_api_key():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key is None:
        print("Error: OPENAI_API_KEY not found. Please check your .env file.")
        return None
    return api_key

def initialize_client(api_key):
    return OpenAI(api_key=api_key)

def categorize_intent_gpt(client, user_input: str) -> str:

    classification_system_prompt = (
        f"You are an intent classification assistant. "
        f"Classify the user request strictly into one of these categories:\n"
        f"{', '.join(INTENTS_LIST)}.\n\n"
        f"If the user request does not match any category, return 'other'. "
        f"Return only the exact category name with no extra text."
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": classification_system_prompt},
            {"role": "user", "content": user_input}
        ]
    )

    category = response.choices[0].message.content.strip().lower()

    if category not in INTENTS_LIST:
        category = "other"

    return category

def chat_gpt(client, prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[INSTRUCTIONS,
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

def turn_on_air_purifier():
    print("Air purifier is now ON.")
    main_purifier()
    turn_on()
    success_message("generate a success message for turning on the air purifier")

def turn_off_air_purifier():
    print("Air purifier is now OFF.")
    main_purifier()
    turn_off()
    success_message("generate a success message for turning off the air purifier")

def increase_purifier():
    print("Increasing air purifier.")
    main_purifier()
    high_purifier()
    success_message("generate a success message for increasing the air purifier")

def decrease_purifier():
    print("Decreasing air purifier.")
    main_purifier()
    low_purifier()
    success_message("generate a success message for decreasing the air purifier")

def get_time():
    get_country()
    success_message("generate a success message for getting the time")

def turn_on_led_light():
    asyncio_turnon()
    success_message("generate a success message for turning on the led light")

def turn_off_led_light():
    asyncio_turnoff()
    success_message("generate a success message for turning off the led light")


def listen_for_input():
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 1.6
    with sr.Microphone() as source:
        print("Speak...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None

async def speak_response(response: str) -> None:
    communicate = edge_tts.Communicate(response, VOICE)
    await communicate.save(OUTPUT_FILE)
    
    pygame.mixer.init()
    pygame.mixer.music.load(OUTPUT_FILE)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def success_message(success_msg: str):
    success_reply = chat_gpt(client, success_msg)
    print(f"GPT Message: {success_reply}")
    asyncio.run(speak_response(success_reply))

def pre_setup():
    print("Setting up connection for quick access")
    connect_sync()

if __name__ == "__main__":
    pre_setup()
    api_key = load_api_key()
    if api_key:
        client = initialize_client(api_key)
        
        while True:
            spoken_text = listen_for_input()
            
            if spoken_text:
                intent = categorize_intent_gpt(client, spoken_text)

                if intent == "turn_on_air_purifier":
                    turn_on_air_purifier()
                elif intent == "turn_off_air_purifier":
                    turn_off_air_purifier()
                elif intent == "increase_purifier":
                    increase_purifier()
                elif intent == "decrease_purifier":
                    decrease_purifier()
                elif intent == "get_time":
                    get_time()
                elif intent == "turn_on_led_light":
                    turn_on_led_light()
                elif intent == "turn_off_led_light":
                    turn_off_led_light()
                else:
                    response = chat_gpt(client, spoken_text)
                    print(f"GPT Response: {response}")
                    asyncio.run(speak_response(response))
            else:
                print("Sorry, I could not understand the audio.")
