"""
Aroha Voice Assistant - System Control Module

This module handles system operations like shutdown, restart, sleep, and lock.
"""

import os
import subprocess
from assistant.speak import speak
import config


def ask_confirmation(action):
    """
    Ask user for confirmation before executing dangerous action.
    
    Args:
        action (str): Action name (e.g., "shutdown")
        
    Returns:
        bool: True if user confirms
    """
    if not config.CONFIRM_DANGEROUS_ACTIONS:
        return True
    
    speak(f"Are you sure you want to {action}? Say yes to confirm.")
    
    from assistant.listen import listen
    response = listen()
    
    if response:
        response = response.lower()
        if "yes" in response or "yeah" in response or "yep" in response or "sure" in response:
            return True
        elif response.startswith("__manual___"):
            manual_response = response.replace("__manual___", "")
            if "yes" in manual_response or manual_response == "y":
                return True
                
    return False


def shutdown_pc():
    """
    Shutdown the computer.
    
    Returns:
        bool: True if successful
    """
    if not config.ENABLE_SYSTEM_CONTROL:
        return False
    
    try:
        if ask_confirmation("shutdown"):
            speak("Shutting down the computer")
            os.system("shutdown /s /t 10")  # Shutdown in 10 seconds
            return True
        else:
            speak("Shutdown cancelled")
            return False
    except Exception as e:
        if config.DEBUG_MODE:
            print(f"[ERROR] Shutdown error: {e}")
        speak("Error shutting down")
        return False


def restart_pc():
    """
    Restart the computer.
    
    Returns:
        bool: True if successful
    """
    if not config.ENABLE_SYSTEM_CONTROL:
        return False
    
    try:
        if ask_confirmation("restart"):
            speak("Restarting the computer")
            os.system("shutdown /r /t 10")  # Restart in 10 seconds
            return True
        else:
            speak("Restart cancelled")
            return False
    except Exception as e:
        if config.DEBUG_MODE:
            print(f"[ERROR] Restart error: {e}")
        speak("Error restarting")
        return False


def sleep_pc():
    """
    Put the computer to sleep.
    
    Returns:
        bool: True if successful
    """
    if not config.ENABLE_SYSTEM_CONTROL:
        return False
    
    try:
        speak("Putting computer to sleep")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        return True
    except Exception as e:
        if config.DEBUG_MODE:
            print(f"[ERROR] Sleep error: {e}")
        speak("Error putting computer to sleep")
        return False


def lock_pc():
    """
    Lock the computer.
    
    Returns:
        bool: True if successful
    """
    if not config.ENABLE_SYSTEM_CONTROL:
        return False
    
    try:
        speak("Locking the computer")
        os.system("rundll32.exe user32.dll,LockWorkStation")
        return True
    except Exception as e:
        if config.DEBUG_MODE:
            print(f"[ERROR] Lock error: {e}")
        speak("Error locking computer")
        return False
