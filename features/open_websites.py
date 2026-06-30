"""
Aroha Voice Assistant - Open Websites Module

This module opens websites stored in data/websites.json
"""

import webbrowser
from assistant.speak import speak
from assistant.utils import load_json, get_data_path
import config


def open_website(command):
    """
    Open a website based on the user command.
    
    Args:
        command (str): User command containing website name
        
    Returns:
        bool: True if successful
    """
    # Load websites data
    websites_data = load_json(get_data_path('websites.json'))
    
    if not websites_data:
        speak("Website list not available")
        return False
    
    command = command.lower()
    
    # Search for matching website
    for name, url in websites_data.get('websites', {}).items():
        if name.lower() in command:
            try:
                speak(f"Opening {name}")
                webbrowser.open(url)
                return True
            except Exception as e:
                if config.DEBUG_MODE:
                    print(f"⚠️  Error opening {name}: {e}")
                speak(f"Could not open {name}")
                return False
    
    # If no match found
    speak("Website not found in my list")
    return False


def list_websites():
    """
    Get list of available websites.
    
    Returns:
        list: List of website names
    """
    websites_data = load_json(get_data_path('websites.json'))
    return list(websites_data.get('websites', {}).keys())
