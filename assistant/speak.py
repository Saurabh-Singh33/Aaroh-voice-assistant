"""
Aroha Voice Assistant - Text-to-Speech Module

This module handles all text-to-speech functionality using pyttsx3.
It provides a clean interface for the assistant to speak responses.
"""

import pyttsx3
import time
import config


class Speaker:
    """
    Handles text-to-speech operations using pyttsx3.
    
    This class manages the TTS engine initialization and provides
    methods to speak text naturally.
    """
    
    def __init__(self):
        """Initialize the text-to-speech engine."""
        try:
            self.engine = pyttsx3.init()
            self.engine.setProperty('rate', config.SPEECH_RATE)
            self.engine.setProperty('volume', config.SPEECH_VOLUME)
            if config.DEBUG_MODE:
                print("[OK] Text-to-Speech engine initialized")
        except Exception as e:
            print(f"[WARNING] Could not initialize TTS engine: {e}")
            self.engine = None
    
    def speak(self, text):
        """
        Speak the given text using text-to-speech.
        
        Args:
            text (str): The text to speak
            
        Returns:
            None
        """
        if not text:
            return
        
        print(f"[AROHA] {text}")
        
        if config.USE_SPEECH and self.engine:
            try:
                self.engine.say(text)
                self.engine.runAndWait()
                time.sleep(config.RESPONSE_DELAY)
            except Exception as e:
                if config.DEBUG_MODE:
                    print(f"[ERROR] TTS Error: {e}")
    
    def set_rate(self, rate):
        """
        Set the speech rate.
        
        Args:
            rate (int): Words per minute (50-300)
        """
        if self.engine:
            self.engine.setProperty('rate', rate)
    
    def set_volume(self, volume):
        """
        Set the speech volume.
        
        Args:
            volume (float): Volume level (0.0 - 1.0)
        """
        if self.engine:
            self.engine.setProperty('volume', volume)
    
    def stop(self):
        """Stop current speech immediately."""
        if self.engine:
            self.engine.stop()


# Global speaker instance
_speaker = None


def initialize_speaker():
    """Initialize the global speaker instance."""
    global _speaker
    _speaker = Speaker()


def speak(text):
    """
    Global function to speak text.
    
    Args:
        text (str): The text to speak
    """
    global _speaker
    if _speaker is None:
        initialize_speaker()
    _speaker.speak(text)


def get_speaker():
    """
    Get the global speaker instance.
    
    Returns:
        Speaker: The speaker instance
    """
    global _speaker
    if _speaker is None:
        initialize_speaker()
    return _speaker
