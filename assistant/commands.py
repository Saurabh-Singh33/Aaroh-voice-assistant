"""Backward-compatible command entry point for Aroha."""

from assistant.ai_service import ai_service
from assistant.intent_router import route_command
from assistant.speak import speak
import config


def process_command(command):
    """Route a command and preserve the original boolean return contract."""
    return process_command_result(command)["success"]


def process_command_result(command):
    """Use local features first, then fall back to the AI Brain if needed."""
    result = route_command(command)
    if result["intent"] != "unknown":
        return result

    ai_result = ai_service.ask(command)
    if ai_result.success:
        speak(ai_result.response)
        return {
            "success": True,
            "intent": "ai_brain",
            "entities": {"query": command},
            "message": "AI response generated",
            "response": ai_result.response,
        }

    if config.DEBUG_MODE:
        print(f"[WARNING] AI Brain unavailable: {ai_result.error}")
    speak("I couldn't answer that right now.")
    return {
        "success": False,
        "intent": "ai_brain",
        "entities": {"query": command},
        "message": "AI response unavailable",
    }


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
