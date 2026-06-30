"""
Aroha Voice Assistant - Speech Recognition Module

This module handles speech recognition using the SpeechRecognition library.
It provides a clean interface to convert voice input to text.
"""

import speech_recognition as sr
import config


class Listener:
    """
    Handles speech recognition operations.
    
    This class manages the microphone input and converts speech to text
    using Google's speech recognition API.
    """
    
    def __init__(self):
        """Initialize the speech recognizer."""
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = config.RECOGNIZER_ENERGY_THRESHOLD
        
        if config.DEBUG_MODE:
            print("✓ Speech recognizer initialized")
    
    def listen(self):
        """
        Listen for speech and convert to text.

        Returns:
            str: The recognized text in lowercase, or None if recognition failed
        """
        for attempt in range(2):
            try:
                with sr.Microphone() as source:
                    # Adjust for ambient noise
                    self.recognizer.adjust_for_ambient_noise(source, duration=0.5)

                    print("🎙️  Listening...")

                    # Listen for audio
                    audio = self.recognizer.listen(
                        source,
                        timeout=config.RECOGNIZER_TIMEOUT,
                        phrase_time_limit=config.RECOGNIZER_PHRASE_TIME_LIMIT
                    )

            except sr.WaitTimeoutError:
                if attempt == 0:
                    print("⚠️  I didn't hear anything. Please try again.")
                    continue
                return None
            except sr.RequestError:
                print("❌ Microphone not available")
                return None
            except sr.UnknownValueError:
                return None
            except Exception as e:
                if config.DEBUG_MODE:
                    print(f"⚠️  Listening error: {e}")
                return None

            # Recognize speech
            try:
                text = self.recognizer.recognize_google(
                    audio,
                    language=config.SYSTEM_LANGUAGE
                )
                return text.lower()

            except sr.UnknownValueError:
                if attempt == 0:
                    print("⚠️  Could not understand audio. Please try again.")
                    continue
                return None
            except sr.RequestError as e:
                print(f"⚠️  API error: {e}")
                return None
            except Exception as e:
                if config.DEBUG_MODE:
                    print(f"⚠️  Recognition error: {e}")
                return None

        return None


# Global listener instance
_listener = None


def initialize_listener():
    """Initialize the global listener instance."""
    global _listener
    _listener = Listener()


def listen():
    """
    Global function to listen for speech.
    
    Returns:
        str: The recognized text in lowercase, or None if recognition failed
    """
    global _listener
    if _listener is None:
        initialize_listener()
    return _listener.listen()


def get_listener():
    """
    Get the global listener instance.
    
    Returns:
        Listener: The listener instance
    """
    global _listener
    if _listener is None:
        initialize_listener()
    return _listener
