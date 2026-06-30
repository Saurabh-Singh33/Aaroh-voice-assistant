"""
Aroha Voice Assistant - Google Search Module

This module opens Google search results in the default web browser.
"""

import webbrowser
from urllib.parse import quote


def search_google(query):
    """
    Open Google search with the given query.
    
    Args:
        query (str): The search query
        
    Returns:
        bool: True if successful
    """
    if not query:
        return False
    
    try:
        # Encode the query for URL
        encoded_query = quote(query)
        search_url = f"https://www.google.com/search?q={encoded_query}"
        
        # Open in default browser
        webbrowser.open(search_url)
        
        return True
    except Exception as e:
        print(f"❌ Error opening Google search: {e}")
        return False
