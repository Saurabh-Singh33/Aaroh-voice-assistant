"""
Aroha Voice Assistant - Music Player Module

This module plays random music from a specified folder.
"""

import os
import random
from assistant.speak import speak
import config


def play_music():
    """
    Play a random song from the music folder.
    
    Returns:
        bool: True if successful
    """
    if not config.ENABLE_MUSIC:
        return False
    
    music_folder = config.MUSIC_FOLDER
    
    if not music_folder:
        speak("Music folder not configured. Please set MUSIC_FOLDER in config.py")
        return False
    
    if not os.path.exists(music_folder):
        speak(f"Music folder not found: {music_folder}")
        return False
    
    try:
        # Get all music files
        music_files = []
        for root, dirs, files in os.walk(music_folder):
            for file in files:
                if any(file.lower().endswith(fmt) for fmt in config.SUPPORTED_AUDIO_FORMATS):
                    music_files.append(os.path.join(root, file))
        
        if not music_files:
            speak("No music files found in the specified folder")
            return False
        
        # Select a random song
        selected_song = random.choice(music_files)
        song_name = os.path.basename(selected_song)
        
        # Play the song
        speak(f"Playing {song_name}")
        
        # Use the default media player
        os.startfile(selected_song)
        
        return True
    
    except Exception as e:
        if config.DEBUG_MODE:
            print(f"[ERROR] Music player error: {e}")
        speak("Error playing music")
        return False
