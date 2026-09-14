"""Natural-language intent routing for Aroha commands."""

from dataclasses import asdict, dataclass
import re

from assistant.speak import speak
import config


@dataclass
class RouterResult:
    """Stable result returned after a command is classified and handled."""

    success: bool
    intent: str
    entities: dict
    message: str = ""

    def to_dict(self):
        return asdict(self)


def normalize_command(command):
    """Normalize speech text without removing useful math operators."""
    if not command:
        return ""
    normalized = command.lower().replace("’", "'")
    return re.sub(r"\s+", " ", normalized).strip(" .?!")


def route_command(command):
    """Classify, extract entities, execute a feature, and return its result."""
    normalized = normalize_command(command)
    if not normalized:
        return RouterResult(False, "unknown", {}, "No command was provided").to_dict()

    intent, entities = _classify(normalized)
    if config.DEBUG_MODE:
        print(f"DEBUG: Intent={intent}, entities={entities}")

    if intent == "unknown":
        return RouterResult(False, intent, entities, "No local feature matched").to_dict()

    if intent == "help":
        _show_help()
        return RouterResult(True, intent, entities, "Help displayed").to_dict()

    handler, args = _handler_for(intent, entities)
    if handler is None:
        speak("That feature is currently disabled.")
        return RouterResult(False, intent, entities, "Feature disabled").to_dict()

    try:
        outcome = handler(*args)
        success = outcome is not False
    except Exception as error:
        if config.DEBUG_MODE:
            print(f"[ERROR] Router error for {intent}: {error}")
        speak("I couldn't complete that command.")
        return RouterResult(False, intent, entities, str(error)).to_dict()

    return RouterResult(success, intent, entities, "Command completed" if success else "Command failed").to_dict()


def _classify(command):
    if _matches(command, ["help", "what can you do", "what do you do", "commands"]):
        return "help", {}
    if "weather" in command:
        return "weather", {"location": _extract_after(command, ["weather like in", "weather in", "weather for", "weather at"])}
    if _is_calculator(command):
        expression = _extract_expression(command)
        return "calculator", {"expression": expression} if expression else {}
    if _matches(command, ["wikipedia", "who is", "what is", "what's", "tell me about"]):
        query = _extract_after(command, ["wikipedia", "who is", "what is", "what's", "tell me about"])
        return "wikipedia_search", {"query": query} if query else {}
    if _is_google_search(command):
        query = _extract_after(command, ["search google for", "search google", "search for", "google", "search"])
        return "google_search", {"query": query} if query else {}
    if _matches(command, ["shutdown", "shut down", "power off"]):
        return "shutdown", {}
    if _matches(command, ["restart", "reboot"]):
        return "restart", {}
    if _matches(command, ["hibernate", "put my computer to sleep", "sleep my computer"]):
        return "sleep", {}
    if "lock" in command and "screen" in command or command.startswith("lock"):
        return "lock", {}
    if _matches(command, ["what time", "current time", "time is it", "tell me the time"]):
        return "time", {}
    if _matches(command, ["today's date", "what is today's date", "what's today's date", "current date"]):
        return "date", {}
    if _matches(command, ["play music", "play a song", "listen to music", "music"]):
        return "music", {}
    if _matches(command, ["tell me a joke", "make me laugh", "say a joke", "tell a joke"]):
        return "joke", {}
    if _matches(command, ["flip a coin", "toss a coin", "coin flip"]):
        return "coin", {}
    if _matches(command, ["open", "launch", "start", "go to", "visit"]):
        return _open_intent(command)
    return "unknown", {}


def _open_intent(command):
    website_cues = ["website", "web site", "browser", "go to", "visit"]
    if any(cue in command for cue in website_cues):
        return "open_website", {"target": command}
    return "open_application", {"target": command}


def _handler_for(intent, entities):
    if intent == "time":
        from features.date_time import get_current_time
        return _speak_value, ("The current time is", get_current_time())
    if intent == "date":
        from features.date_time import get_current_date
        return _speak_value, ("Today's date is", get_current_date())
    if intent == "google_search":
        from features.google_search import search_google
        return search_google, (entities.get("query", ""),)
    if intent == "wikipedia_search":
        from features.wikipedia_search import search_wikipedia
        return search_wikipedia, (entities.get("query", ""),)
    if intent == "weather" and config.ENABLE_WEATHER:
        from features.weather import get_weather
        return get_weather, (entities.get("location"),)
    if intent == "calculator" and config.ENABLE_CALCULATOR:
        from features.calculator import calculate
        return calculate, (entities.get("expression", ""),)
    if intent == "music" and config.ENABLE_MUSIC:
        from features.music import play_music
        return play_music, ()
    if intent == "joke" and getattr(config, "ENABLE_FUN", True):
        from features.fun import tell_joke
        return tell_joke, ()
    if intent == "coin" and getattr(config, "ENABLE_FUN", True):
        from features.fun import flip_coin
        return flip_coin, ()
    if intent == "open_application":
        from features.open_apps import open_application
        return open_application, (entities.get("target", ""),)
    if intent == "open_website":
        from features.open_websites import open_website
        return open_website, (entities.get("target", ""),)
    if intent in {"shutdown", "restart", "sleep", "lock"} and config.ENABLE_SYSTEM_CONTROL:
        from features import system_control
        return getattr(system_control, {"shutdown": "shutdown_pc", "restart": "restart_pc", "sleep": "sleep_pc", "lock": "lock_pc"}[intent]), ()
    return None, ()


def _is_google_search(command):
    return any(phrase in command for phrase in ["search", "google search", "search google"])


def _is_calculator(command):
    return "calculate" in command or "percent of" in command or bool(re.search(r"\d\s*[+*/-]\s*\d", command))


def _extract_after(command, phrases):
    for phrase in phrases:
        if phrase in command:
            return command.split(phrase, 1)[1].strip(" .?!")
    return ""


def _extract_expression(command):
    expression = _extract_after(command, ["calculate", "what is", "what's"])
    if not expression and "percent of" in command:
        expression = command
    percent_match = re.fullmatch(r"(?:calculate )?(\d+(?:\.\d+)?) percent of (\d+(?:\.\d+)?)", expression)
    if percent_match:
        return f"({percent_match.group(1)} / 100) * {percent_match.group(2)}"
    return expression


def _matches(command, phrases):
    return any(phrase in command for phrase in phrases)


def _speak_value(prefix, value):
    speak(f"{prefix} {value}")
    return True


def _show_help():
    speak("I can help with time, date, search, websites, applications, weather, music, calculator, fun features, and system control.")