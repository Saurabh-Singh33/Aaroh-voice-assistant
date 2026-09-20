"""Memory policy and spoken operations, kept separate from the AI Brain."""

import re
import sqlite3

import config
from assistant.memory_store import MemoryStore
from assistant.speak import speak


_SENSITIVE_TERMS = {
    "password", "passcode", "pin", "secret", "api key", "apikey",
    "access token", "credit card", "bank account", "social security",
}


def _store():
    return MemoryStore(
        config.MEMORY_DATABASE_PATH,
        config.MEMORY_MAX_ITEMS,
        config.MEMORY_MAX_VALUE_LENGTH,
    )


def remember(memory_text):
    """Persist only an explicit, non-sensitive preference statement."""
    parsed = _parse_memory(memory_text)
    if not parsed:
        speak("Tell me what to remember, such as your favorite language.")
        return False
    key, value = parsed
    if _is_sensitive(f"{key} {value}"):
        speak("I won't store passwords, secrets, financial details, or other sensitive information.")
        return False
    try:
        _store().save(key, value)
    except (OSError, sqlite3.Error, ValueError) as error:
        if config.DEBUG_MODE:
            print(f"[ERROR] Memory save failed: {error}")
        speak("I couldn't save that memory.")
        return False
    speak(f"I'll remember that your {key} is {value}.")
    return True


def recall(query=""):
    try:
        memories = _store().list(query)
    except (OSError, sqlite3.Error):
        speak("I couldn't read my memory right now.")
        return False
    if not memories:
        speak("I don't have any matching memories about you.")
        return True
    spoken = "; ".join(f"your {item['memory_key']} is {item['memory_value']}" for item in memories)
    speak(f"I remember {spoken}.")
    return True


def forget(query):
    query = re.sub(r"^(?:my\s+)?(?:preference|favorite|favourite)\s+for\s+", "", query.strip(), flags=re.IGNORECASE)
    if _is_sensitive(query):
        speak("I don't store sensitive information, so there is nothing to remove.")
        return True
    try:
        deleted = _store().delete(query)
    except (OSError, sqlite3.Error):
        speak("I couldn't update my memory right now.")
        return False
    speak("I've forgotten that memory." if deleted else "I couldn't find a matching memory.")
    return True


def search(query):
    return recall(query)


def get_context(query=""):
    """Return bounded, non-sensitive text for the AI Brain prompt."""
    try:
        memories = _store().list(query)[:config.MEMORY_CONTEXT_LIMIT]
    except (OSError, sqlite3.Error):
        return ""
    return "; ".join(f"{item['memory_key']}: {item['memory_value']}" for item in memories)


def _parse_memory(text):
    text = re.sub(r"^that\s+", "", text.strip(), flags=re.IGNORECASE)
    match = re.match(r"(?:my\s+)?(.+?)\s+(?:is|are|=)\s+(.+)$", text, re.IGNORECASE)
    if match:
        return _normalize_key(match.group(1)), match.group(2).strip(" .?!")
    match = re.match(r"(?:i\s+)?prefer\s+(.+)$", text, re.IGNORECASE)
    if match:
        return "preference", match.group(1).strip(" .?!")
    return None


def _normalize_key(key):
    key = re.sub(r"^(favorite|favourite)\s+", "favorite ", key.strip(), flags=re.IGNORECASE)
    return key.lower()


def _is_sensitive(text):
    lowered = text.lower()
    return any(term in lowered for term in _SENSITIVE_TERMS)