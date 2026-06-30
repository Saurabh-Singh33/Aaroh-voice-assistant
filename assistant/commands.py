"""
Aroha Voice Assistant - Command Processing Module

This module processes user commands and routes them to the appropriate features.
It acts as the main dispatcher for all assistant functionality.
"""

from assistant.speak import speak
from assistant.wake_word import extract_command_from_wake_word
import config


def process_command(command):
    """
    Process the user's command and route to the appropriate feature.
    
    Args:
        command (str): The user's command
        
    Returns:
        bool: True if command was processed, False otherwise
    """
    if not command:
        return False
    
    command = command.lower().strip()
    
    if config.DEBUG_MODE:
        print(f"DEBUG: Processing command: {command}")
    
    # ========== Help Command ==========
    if _is_help_command(command):
        show_help()
        return True
    
    # ========== Date and Time Commands ==========
    if _is_time_command(command):
        from features.date_time import get_current_time
        time_str = get_current_time()
        speak(f"The current time is {time_str}")
        return True
    
    if _is_date_command(command):
        from features.date_time import get_current_date
        date_str = get_current_date()
        speak(f"Today's date is {date_str}")
        return True
    
    # ========== Search Commands ==========
    if _is_search_command(command):
        from features.google_search import search_google
        query = command.replace("search", "", 1).strip()
        if query:
            search_google(query)
            speak(f"Searching Google for {query}")
        else:
            speak("What would you like me to search for?")
        return True
    
    if _is_wikipedia_command(command):
        from features.wikipedia_search import search_wikipedia
        query = command.replace("wikipedia", "", 1).replace("who is", "", 1).replace("what is", "", 1).strip()
        if query:
            search_wikipedia(query)
        else:
            speak("What would you like to search on Wikipedia?")
        return True
    
    # ========== Website Commands ==========
    if _is_website_command(command):
        from features.open_websites import open_website
        open_website(command)
        return True
    
    # ========== Application Commands ==========
    if _is_app_command(command):
        from features.open_apps import open_application
        open_application(command)
        return True
    
    # ========== Weather Command ==========
    if _is_weather_command(command) and config.ENABLE_WEATHER:
        from features.weather import get_weather
        location = _extract_location(command)
        if location:
            get_weather(location)
        else:
            speak("Which location's weather would you like to know?")
        return True
    
    # ========== Calculator Command ==========
    if _is_calculator_command(command) and config.ENABLE_CALCULATOR:
        from features.calculator import calculate
        expression = _extract_expression(command)
        if expression:
            calculate(expression)
        else:
            speak("What calculation would you like me to perform?")
        return True
    
    # ========== Music Command ==========
    if _is_music_command(command) and config.ENABLE_MUSIC:
        from features.music import play_music
        play_music()
        return True
    
    # ========== System Control Commands ==========
    if _is_shutdown_command(command) and config.ENABLE_SYSTEM_CONTROL:
        from features.system_control import shutdown_pc
        shutdown_pc()
        return True
    
    if _is_restart_command(command) and config.ENABLE_SYSTEM_CONTROL:
        from features.system_control import restart_pc
        restart_pc()
        return True
    
    if _is_sleep_command(command) and config.ENABLE_SYSTEM_CONTROL:
        from features.system_control import sleep_pc
        sleep_pc()
        return True
    
    if _is_lock_command(command) and config.ENABLE_SYSTEM_CONTROL:
        from features.system_control import lock_pc
        lock_pc()
        return True
    
    # ========== Unknown Command ==========
    speak("I didn't understand that. Say 'Help' for available commands.")
    return False


# ============================================================================
# COMMAND DETECTION FUNCTIONS
# ============================================================================

def _is_help_command(command):
    """Check if command is asking for help."""
    help_keywords = ["help", "what can you do", "commands", "what do you do"]
    return any(keyword in command for keyword in help_keywords)


def _is_time_command(command):
    """Check if command is asking for time."""
    time_keywords = ["time", "current time", "what time"]
    return any(keyword in command for keyword in time_keywords)


def _is_date_command(command):
    """Check if command is asking for date."""
    date_keywords = ["date", "today", "what's today", "what is today"]
    return any(keyword in command for keyword in date_keywords)


def _is_search_command(command):
    """Check if command is a Google search."""
    return command.startswith("search") or "search for" in command


def _is_wikipedia_command(command):
    """Check if command is a Wikipedia search."""
    wiki_keywords = ["wikipedia", "who is", "what is"]
    return any(keyword in command for keyword in wiki_keywords) and "weather" not in command


def _is_website_command(command):
    """Check if command is to open a website."""
    website_keywords = ["open", "go to", "visit"]
    return any(keyword in command for keyword in website_keywords)


def _is_app_command(command):
    """Check if command is to open an application."""
    app_keywords = ["open", "launch", "start"]
    return any(keyword in command for keyword in app_keywords)


def _is_weather_command(command):
    """Check if command is asking for weather."""
    return "weather" in command


def _is_calculator_command(command):
    """Check if command is a calculation."""
    # Check for mathematical operators
    operators = ["+", "-", "*", "/", "plus", "minus", "times", "divide", "calculate"]
    return any(op in command for op in operators)


def _is_music_command(command):
    """Check if command is to play music."""
    music_keywords = ["play music", "music", "song"]
    return any(keyword in command for keyword in music_keywords)


def _is_shutdown_command(command):
    """Check if command is to shutdown PC."""
    shutdown_keywords = ["shutdown", "shut down", "power off"]
    return any(keyword in command for keyword in shutdown_keywords)


def _is_restart_command(command):
    """Check if command is to restart PC."""
    restart_keywords = ["restart", "reboot"]
    return any(keyword in command for keyword in restart_keywords)


def _is_sleep_command(command):
    """Check if command is to sleep PC."""
    sleep_keywords = ["sleep", "hibernate"]
    return any(keyword in command for keyword in sleep_keywords)


def _is_lock_command(command):
    """Check if command is to lock PC."""
    lock_keywords = ["lock", "lock screen"]
    return any(keyword in command for keyword in lock_keywords)


# ============================================================================
# COMMAND EXTRACTION FUNCTIONS
# ============================================================================

def _extract_location(command):
    """Extract location from weather command."""
    keywords = ["weather in", "weather for", "weather at"]
    for keyword in keywords:
        if keyword in command:
            return command.split(keyword)[-1].strip()
    return None


def _extract_expression(command):
    """Extract mathematical expression from calculator command."""
    # Remove command keywords
    expression = command.replace("calculate", "").replace("what is", "").strip()
    return expression if expression else None


# ============================================================================
# HELP AND UTILITY FUNCTIONS
# ============================================================================

def show_help():
    """Display available commands to the user."""
    help_text = """
    Here are the commands I understand:
    
    TIME & DATE:
    - "What time is it?" - Tell current time
    - "What's today's date?" - Tell current date
    
    SEARCH:
    - "Search [topic]" - Google search
    - "Who is [person]?" - Wikipedia search
    
    WEBSITES:
    - "Open YouTube/Google/GitHub/Gmail/LinkedIn"
    
    APPLICATIONS:
    - "Open Chrome/VS Code/Notepad/Calculator/Paint"
    
    FEATURES:
    - "What's the weather in [city]?"
    - "Play music"
    - "Calculate [expression]"
    - "Shutdown/Restart/Sleep/Lock PC"
    
    OTHER:
    - "Help" - Show this message
    - "Exit/Goodbye" - Stop listening
    """
    
    speak("I can help with time, date, search, websites, applications, weather, music, calculator, and system control.")
    print(help_text)
