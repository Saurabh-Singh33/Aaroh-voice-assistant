"""
Aroha Voice Assistant - Calculator Module

This module evaluates simple mathematical expressions.
"""

from assistant.speak import speak
import config


def calculate(expression):
    """
    Evaluate a mathematical expression and speak the result.
    
    Args:
        expression (str): Mathematical expression (e.g., "15 + 22")
        
    Returns:
        bool: True if successful
    """
    if not expression or not config.ENABLE_CALCULATOR:
        return False
    
    try:
        # Convert word operators to symbols
        expression = expression.replace(" plus ", " + ")
        expression = expression.replace(" minus ", " - ")
        expression = expression.replace(" times ", " * ")
        expression = expression.replace(" multiplied by ", " * ")
        expression = expression.replace(" divide ", " / ")
        expression = expression.replace(" divided by ", " / ")
        expression = expression.replace(" into ", " / ")
        
        # Remove spaces for evaluation
        expression = expression.replace(" ", "")
        
        # Evaluate the expression
        result = eval(expression)
        
        # Ensure result is a number
        if isinstance(result, (int, float)):
            # Format the result
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            
            # Speak the result
            speak(f"The answer is {result}")
            return True
        else:
            speak("Invalid calculation")
            return False
    
    except ZeroDivisionError:
        speak("Cannot divide by zero")
        return False
    except SyntaxError:
        speak("Invalid mathematical expression")
        return False
    except Exception as e:
        if config.DEBUG_MODE:
            print(f"[ERROR] Calculator error: {e}")
        speak("Error calculating the expression")
        return False
