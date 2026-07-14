"""
Aroha Voice Assistant - Speech Recognition Module

This module handles speech recognition using the SpeechRecognition library.
It provides a clean interface to convert voice input to text.
"""

import speech_recognition as sr
import config


def get_microphone_device_index():
    """Pick the most likely physical microphone device on Windows."""
    try:
        devices = sr.Microphone.list_microphone_names()
    except Exception:
        return 0

    for index, device_name in enumerate(devices):
        name = (device_name or "").lower()
        if not name:
            continue
        if any(token in name for token in ["microphone", "mic", "array"]):
            if any(token in name for token in ["mapper", "output", "speaker", "stereo", "headphone"]):
                continue
            return index

    return 0


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
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.dynamic_energy_adjustment_damping = 0.15
        self.recognizer.dynamic_energy_ratio = 1.5
        self.recognizer.pause_threshold = 0.8
        self.microphone_index = None

        if config.DEBUG_MODE:
            print("[OK] Speech recognizer initialized")
    
    def listen(self):
        """
        Listen for speech and convert to text.

        Returns:
            str: The recognized text in lowercase, or None if recognition failed
        """
        for attempt in range(3):
            try:
                with sr.Microphone(device_index=self.microphone_index) as source:
                    self.recognizer.adjust_for_ambient_noise(source, duration=0.5)

                    print("[LISTENING] Listening for input...")

                    audio = self.recognizer.listen(
                        source,
                        timeout=config.RECOGNIZER_TIMEOUT,
                        phrase_time_limit=config.RECOGNIZER_PHRASE_TIME_LIMIT
                    )

            except sr.WaitTimeoutError:
                if attempt < 2:
                    print("[WARNING] I didn't hear anything. Please try again.")
                    continue
                break
            except sr.RequestError:
                print("[ERROR] Microphone not available")
                break
            except sr.UnknownValueError:
                break
            except Exception as e:
                if config.DEBUG_MODE:
                    print(f"[WARNING] Listening error: {e}")
                break

            try:
                text = self.recognizer.recognize_google(
                    audio,
                    language=config.SYSTEM_LANGUAGE
                )
                return text.lower()

            except sr.UnknownValueError:
                if attempt < 2:
                    print("[WARNING] Could not understand audio. Please try again.")
                    continue
            except sr.RequestError as e:
                print(f"[WARNING] Speech recognition API error: {e}")
            except Exception as e:
                if config.DEBUG_MODE:
                    print(f"[ERROR] Recognition error: {e}")

        if config.FALLBACK_TO_MANUAL_INPUT:
            print("[TEXT INPUT] Voice input is unavailable right now. Type a command instead.")
            try:
                manual_input = input("You: ").strip()
                if manual_input:
                    return manual_input.lower()
            except EOFError:
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
