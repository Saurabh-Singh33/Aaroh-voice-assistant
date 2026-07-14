"""
Aroha Voice Assistant - Fun Features

This module handles fun and interactive features like telling jokes
and flipping coins.
"""

import random
import requests
from assistant.speak import speak
import config

def tell_joke():
    """Fetches a random joke from an API and speaks it."""
    try:
        if config.DEBUG_MODE:
            print("Fetching a joke...")
        
        response = requests.get("https://official-joke-api.appspot.com/random_joke", timeout=5)
        if response.status_code == 200:
            joke = response.json()
            setup = joke.get("setup", "")
            punchline = joke.get("punchline", "")
            
            print(f"Joke: {setup} - {punchline}")
            speak(setup)
            # Speak the punchline after
            speak(punchline)
        else:
            speak("I couldn't think of a joke right now, sorry!")
            
    except Exception as e:
        if config.DEBUG_MODE:
            print(f"Error fetching joke: {e}")
        speak("My joke module seems to be offline.")

def flip_coin():
    """Flips a coin and speaks the result."""
    result = random.choice(["heads", "tails"])
    print(f"Coin flip result: {result.upper()}")
    speak(f"I flipped a coin and it landed on {result}.")
