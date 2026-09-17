"""
Aroha Voice Assistant - Configuration Module

This module contains all configuration settings for the Aroha voice assistant.
Centralized configuration allows for easy customization without modifying code.
"""

import os

from dotenv import load_dotenv

load_dotenv()

# ============================================================================
# WAKE WORD SETTINGS
# ============================================================================
WAKE_WORDS = ["hey aroha", "aroha"]
WAKE_WORD_CONFIDENCE = 0.7  # Confidence threshold for wake word detection (0.0 - 1.0)

# ============================================================================
# SPEECH RECOGNITION SETTINGS
# ============================================================================
RECOGNIZER_TIMEOUT = 8  # Seconds to wait for speech input
RECOGNIZER_PHRASE_TIME_LIMIT = 10  # Max duration of audio to record
RECOGNIZER_ENERGY_THRESHOLD = 3000  # Microphone energy threshold
FALLBACK_TO_MANUAL_INPUT = True  # Let the user type commands if voice recognition fails

# ============================================================================
# TEXT-TO-SPEECH SETTINGS
# ============================================================================
SPEECH_RATE = 150  # Words per minute (default: 200)
SPEECH_VOLUME = 0.9  # Volume level (0.0 - 1.0)
USE_SPEECH = True  # Enable/disable audio output

# ============================================================================
# WEATHER API SETTINGS
# ============================================================================
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "")
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"

# ============================================================================
# MUSIC SETTINGS
# ============================================================================
MUSIC_FOLDER = None  # Set to your music folder path, e.g., "C:/Users/YourName/Music"
SUPPORTED_AUDIO_FORMATS = [".mp3", ".wav", ".flac", ".ogg"]

# ============================================================================
# APPLICATION PATHS (Windows-specific, can be customized)
# ============================================================================
# Note: Apps are also stored in data/apps.json for easier management
SYSTEM_LANGUAGE = "en-US"  # For speech recognition
SYSTEM_TTS_VOICE = "en"  # Text-to-speech language

# ============================================================================
# FEATURE FLAGS
# ============================================================================
ENABLE_WIKIPEDIA = True
ENABLE_WEATHER = True
ENABLE_CALCULATOR = True
ENABLE_MUSIC = True
ENABLE_SYSTEM_CONTROL = True
ENABLE_FUN = True

# ============================================================================
# LOGGING AND DEBUGGING
# ============================================================================
DEBUG_MODE = True  # Set to True for verbose logging
LOG_FILE = "aroha.log"

# ============================================================================
# AI BRAIN SETTINGS
# ============================================================================
AI_ENABLED = os.getenv("AROHA_AI_ENABLED", "true").lower() in {"1", "true", "yes", "on"}
AI_API_KEY = os.getenv("AROHA_AI_API_KEY", "")
AI_BASE_URL = os.getenv("AROHA_AI_BASE_URL", "https://api.openai.com/v1/chat/completions")
AI_MODEL = os.getenv("AROHA_AI_MODEL", "gpt-4o-mini")
AI_TIMEOUT_SECONDS = float(os.getenv("AROHA_AI_TIMEOUT_SECONDS", "20"))
AI_MAX_HISTORY_MESSAGES = int(os.getenv("AROHA_AI_MAX_HISTORY_MESSAGES", "12"))
AI_SYSTEM_PROMPT = os.getenv(
	"AROHA_AI_SYSTEM_PROMPT",
	"You are Aroha, a concise and helpful voice assistant. "
	"Answer clearly and avoid unnecessary formatting for spoken responses.",
)

# ============================================================================
# MEMORY SETTINGS
# ============================================================================
MEMORY_DATABASE_PATH = os.getenv("AROHA_MEMORY_DATABASE", os.path.join("data", "aroha_memory.sqlite3"))
MEMORY_MAX_ITEMS = int(os.getenv("AROHA_MEMORY_MAX_ITEMS", "100"))
MEMORY_MAX_VALUE_LENGTH = int(os.getenv("AROHA_MEMORY_MAX_VALUE_LENGTH", "240"))
MEMORY_CONTEXT_LIMIT = int(os.getenv("AROHA_MEMORY_CONTEXT_LIMIT", "10"))

# ============================================================================
# ASSISTANT BEHAVIOR
# ============================================================================
LISTEN_CONTINUOUSLY = True  # Keep listening after each command
CONFIRM_DANGEROUS_ACTIONS = True  # Ask before shutdown/restart
RESPONSE_DELAY = 0.5  # Delay before speaking response (seconds)
