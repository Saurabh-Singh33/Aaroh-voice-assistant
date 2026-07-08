"""
Aroha Voice Assistant - Open Applications Module

This module launches applications stored in data/apps.json
"""

import subprocess
import os
from assistant.speak import speak
from assistant.utils import load_json, get_data_path
import config


def open_application(command):
    """
    Open an application based on the user command.
    
    Args:
        command (str): User command containing app name
        
    Returns:
        bool: True if successful
    """
    # Load apps data
    apps_data = load_json(get_data_path('apps.json'))
    
    if not apps_data:
        speak("Application list not available")
        return False
    
    command = command.lower()
    
    # Search for matching application
    for app_name, app_path in apps_data.get('applications', {}).items():
        if app_name.lower() in command:
            try:
                speak(f"Opening {app_name}")
                
                if os.path.exists(app_path):
                    subprocess.Popen(app_path)
                    return True
                else:
                    speak(f"Could not find {app_name} at {app_path}")
                    if config.DEBUG_MODE:
                        print(f"[WARNING] App path not found: {app_path}")
                    return False
            
            except Exception as e:
                if config.DEBUG_MODE:
                    print(f"[ERROR] Error opening {app_name}: {e}")
                speak(f"Could not open {app_name}")
                return False
    
    # If no match found
    speak("Application not found in my list")
    return False


def list_applications():
    """
    Get list of available applications.
    
    Returns:
        list: List of application names
    """
    apps_data = load_json(get_data_path('apps.json'))
    return list(apps_data.get('applications', {}).keys())
