"""
Aroha Voice Assistant - Wikipedia Search Module

This module searches Wikipedia and reads the summary aloud.
"""

import wikipedia
from assistant.speak import speak
import config


def search_wikipedia(query):
    """
    Search Wikipedia and speak the summary.
    
    Args:
        query (str): The search query
        
    Returns:
        bool: True if successful
    """
    if not query or not config.ENABLE_WIKIPEDIA:
        return False
    
    try:
        # Search Wikipedia
        results = wikipedia.search(query, results=1)
        
        if not results:
            speak(f"I couldn't find any Wikipedia articles about {query}")
            return False
        
        # Get the page
        page = wikipedia.page(results[0])
        
        # Get the summary (first 2-3 sentences)
        summary = page.summary[:500]  # Limit to 500 characters
        
        # Speak the summary
        speak(f"According to Wikipedia, {summary}")
        
        return True
    
    except wikipedia.exceptions.DisambiguationError as e:
        speak(f"There are multiple results for {query}. Please be more specific.")
        return False
    except wikipedia.exceptions.PageError:
        speak(f"I couldn't find a Wikipedia page for {query}")
        return False
    except Exception as e:
        if config.DEBUG_MODE:
            print(f"[ERROR] Wikipedia error: {e}")
        speak(f"Error searching Wikipedia: {str(e)}")
        return False
