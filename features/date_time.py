"""
Aroha Voice Assistant - Date and Time Module

This module provides functions to get current date and time.
"""

from datetime import datetime


def get_current_time():
    """
    Get the current time in HH:MM AM/PM format.
    
    Returns:
        str: Formatted time string
    """
    now = datetime.now()
    time_str = now.strftime("%I:%M %p")  # 12-hour format with AM/PM
    return time_str


def get_current_date():
    """
    Get the current date in readable format.
    
    Returns:
        str: Formatted date string
    """
    now = datetime.now()
    # Format: Monday, January 15, 2026
    date_str = now.strftime("%A, %B %d, %Y")
    return date_str


def get_current_datetime():
    """
    Get both date and time.
    
    Returns:
        tuple: (date_str, time_str)
    """
    return get_current_date(), get_current_time()
