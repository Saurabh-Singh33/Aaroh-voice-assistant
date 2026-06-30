"""
Aroha Voice Assistant - Utility Functions Module

This module provides helper functions used across the assistant.
"""

import json
import os
import config


def load_json(file_path):
    """
    Load data from a JSON file.
    
    Args:
        file_path (str): Path to the JSON file
        
    Returns:
        dict: Loaded JSON data, or empty dict if file doesn't exist
    """
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
    except Exception as e:
        if config.DEBUG_MODE:
            print(f"⚠️  Error loading {file_path}: {e}")
    
    return {}


def save_json(file_path, data):
    """
    Save data to a JSON file.
    
    Args:
        file_path (str): Path to the JSON file
        data (dict): Data to save
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        if config.DEBUG_MODE:
            print(f"⚠️  Error saving {file_path}: {e}")
        return False


def get_project_root():
    """
    Get the project root directory.
    
    Returns:
        str: Absolute path to project root
    """
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_data_path(filename):
    """
    Get the path to a data file.
    
    Args:
        filename (str): Name of the file in the data directory
        
    Returns:
        str: Absolute path to the data file
    """
    return os.path.join(get_project_root(), 'data', filename)


def sanitize_input(text):
    """
    Sanitize and clean user input.
    
    Args:
        text (str): Input text
        
    Returns:
        str: Cleaned text
    """
    if not text:
        return ""
    
    return text.strip().lower()


def format_output(text):
    """
    Format text for output.
    
    Args:
        text (str): Text to format
        
    Returns:
        str: Formatted text
    """
    if not text:
        return ""
    
    # Capitalize first letter of each sentence
    return text[0].upper() + text[1:] if text else ""
