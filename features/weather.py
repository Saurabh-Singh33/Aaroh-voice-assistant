"""
Aroha Voice Assistant - Weather Module

This module fetches weather information using OpenWeatherMap API.
"""

import requests
from assistant.speak import speak
import config


def get_weather(location):
    """
    Get weather information for a location.
    
    Args:
        location (str): City name
        
    Returns:
        bool: True if successful
    """
    if not location or not config.ENABLE_WEATHER:
        speak("Please specify a location")
        return False
    
    try:
        # Prepare API request
        params = {
            'q': location,
            'appid': config.WEATHER_API_KEY,
            'units': 'metric'  # Use Celsius
        }
        
        # Make request
        response = requests.get(config.WEATHER_API_URL, params=params, timeout=5)
        
        if response.status_code != 200:
            speak(f"Could not find weather for {location}")
            return False
        
        # Parse response
        data = response.json()
        
        # Extract weather information
        temperature = data['main']['temp']
        weather_desc = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        
        # Format and speak response
        weather_text = f"""
        In {location}, the weather is {weather_desc}. 
        Temperature is {temperature} degrees Celsius.
        Humidity is {humidity} percent.
        Wind speed is {wind_speed} meters per second.
        """
        
        speak(weather_text.strip())
        return True
    
    except requests.exceptions.Timeout:
        speak("Weather request timed out. Please try again.")
        return False
    except requests.exceptions.ConnectionError:
        speak("Could not connect to weather service")
        return False
    except Exception as e:
        if config.DEBUG_MODE:
            print(f"⚠️  Weather error: {e}")
        speak("Error fetching weather information")
        return False
