"""Backward-compatible command entry point for Aroha."""

from assistant.intent_router import route_command
from assistant.speak import speak


def process_command(command):
    """Route a command and preserve the original boolean return contract."""
    result = route_command(command)
    return result["success"]


def show_help():
    """Display the existing help response for callers that use it directly."""
    speak("I can help with time, date, search, websites, applications, weather, music, calculator, fun features, and system control.")
    print("""
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
    - "Tell me a joke"
    - "Flip a coin"
    - "Shutdown/Restart/Sleep/Lock PC"

    OTHER:
    - "Help" - Show this message
    - "Exit/Goodbye" - Stop listening
    """)
