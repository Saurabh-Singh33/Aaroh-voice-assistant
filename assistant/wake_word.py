"""
Aroha Voice Assistant - Wake Word Detection Module

This module detects the wake word to activate the assistant.
It provides resilient keyword matching for wake word detection.
"""

import re
from difflib import SequenceMatcher

import config


def _normalize_text(user_input):
    """Normalize text so punctuation and extra spacing do not break matching."""
    if not user_input:
        return ""

    text = user_input.lower().strip()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def detect_wake_word(user_input):
    """
    Detect if the user input contains the wake word.

    Args:
        user_input (str): The user's speech input

    Returns:
        bool: True if wake word is detected, False otherwise
    """
    normalized_input = _normalize_text(user_input)
    if not normalized_input:
        return False

    for wake_word in config.WAKE_WORDS:
        wake_word_lower = _normalize_text(wake_word)
        if not wake_word_lower:
            continue

        if wake_word_lower in normalized_input:
            return True

        words = normalized_input.split()
        if wake_word_lower.split()[0] in words:
            return True

        similarity = SequenceMatcher(None, normalized_input, wake_word_lower).ratio()
        if similarity >= 0.75:
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
    normalized_input = _normalize_text(user_input)
    if not normalized_input:
        return ""

    for wake_word in config.WAKE_WORDS:
        wake_word_lower = _normalize_text(wake_word)
        if not wake_word_lower:
            continue

        if wake_word_lower in normalized_input:
            command = normalized_input.replace(wake_word_lower, "", 1).strip()
            return command

    return normalized_input
