"""
Aroha Voice Assistant - Configuration Module

This module contains all configuration settings for the Aroha voice assistant.
Centralized configuration allows for easy customization without modifying code.
"""

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
WEATHER_API_KEY = "4d8fb5b93d4af21d66a2948710284366"  # OpenWeatherMap Free API
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
DEBUG_MODE = False  # Set to True for verbose logging
LOG_FILE = "aroha.log"

# ============================================================================
# ASSISTANT BEHAVIOR
# ============================================================================
LISTEN_CONTINUOUSLY = True  # Keep listening after each command
CONFIRM_DANGEROUS_ACTIONS = True  # Ask before shutdown/restart
RESPONSE_DELAY = 0.5  # Delay before speaking response (seconds)
