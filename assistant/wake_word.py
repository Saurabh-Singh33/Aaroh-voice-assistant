"""
Aroha Voice Assistant - Wake Word Detection Module

This module detects the wake word to activate the assistant.
It provides simple keyword matching for wake word detection.
"""

import config


def detect_wake_word(user_input):
    """
    Detect if the user input contains the wake word.
    
    Args:
        user_input (str): The user's speech input (already lowercased)
        
    Returns:
        bool: True if wake word is detected, False otherwise
    """
    if not user_input:
        return False
    
    user_input = user_input.lower().strip()
    
    # Check if any wake word is in the user input
    for wake_word in config.WAKE_WORDS:
        if wake_word.lower() in user_input:
            return True
    
    return False


def extract_command_from_wake_word(user_input):
    """
    Extract the command part after the wake word.
    
    Args:
        user_input (str): The user's speech input
        
    Returns:
        str: The command text without the wake word
    """
    if not user_input:
        return ""
    
    user_input = user_input.lower().strip()
    
    for wake_word in config.WAKE_WORDS:
        wake_word_lower = wake_word.lower()
        if wake_word_lower in user_input:
            # Remove the wake word and return the rest
            command = user_input.replace(wake_word_lower, "", 1).strip()
            return command
    
    return user_input
