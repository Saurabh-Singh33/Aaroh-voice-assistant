"""
Aroha Voice Assistant - Main Entry Point

This is the main module that initializes and runs the Aroha voice assistant.
It coordinates between listening, wake word detection, command processing, and features.

Run with: python main.py
"""

import sys
import os

# Add parent directory to path for module imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from assistant.listen import listen
from assistant.speak import speak
from assistant.commands import process_command
from assistant.wake_word import detect_wake_word
import config


class ArohaAssistant:
    """
    Main Aroha Voice Assistant class that orchestrates all functionality.
    
    This class manages the core loop of listening for the wake word,
    processing commands, and executing features.
    """
    
    def __init__(self):
        """Initialize the Aroha assistant."""
        self.is_running = True
        self.wake_word_detected = False
        
        print("\n" + "="*60)
        print("🎤 AROHA VOICE ASSISTANT STARTING...")
        print("="*60)
        print(f"Wake words: {', '.join(config.WAKE_WORDS)}")
        print("Say 'Hey Aroha' to begin. Say 'Exit' to quit.\n")
        
        speak("Aroha is ready. Say 'Hey Aroha' to begin.")
    
    def run(self):
        """
        Main loop that continuously listens for wake word and processes commands.
        
        The assistant:
        1. Listens for the wake word
        2. Once detected, listens for commands
        3. Processes and executes the command
        4. Returns to listening for wake word
        """
        try:
            while self.is_running:
                # Listen for wake word
                print("\n📢 Listening for wake word...")
                user_input = listen()
                
                if user_input is None:
                    continue
                
                # Check for exit commands
                if self._should_exit(user_input):
                    self.exit_assistant()
                    break
                
                # Detect wake word
                if detect_wake_word(user_input):
                    print("\n✓ Wake word detected!")
                    speak("I'm listening. What would you like?")
                    
                    # Listen for command
                    print("📢 Listening for command...")
                    command = listen()
                    
                    if command and not self._should_exit(command):
                        # Process the command
                        process_command(command)
                    elif command:
                        self.exit_assistant()
                        break
        
        except KeyboardInterrupt:
            print("\n\n⚠️  Interrupted by user")
            self.exit_assistant()
        except Exception as e:
            print(f"\n❌ An error occurred: {e}")
            speak("An error occurred. Please try again.")
    
    def _should_exit(self, user_input):
        """
        Check if user wants to exit.
        
        Args:
            user_input (str): The user's speech input
            
        Returns:
            bool: True if exit command detected
        """
        exit_commands = ["exit", "quit", "goodbye", "stop", "stop listening", "bye"]
        return any(cmd in user_input.lower() for cmd in exit_commands)
    
    def exit_assistant(self):
        """Exit the assistant gracefully."""
        print("\n" + "="*60)
        speak("Thank you for using Aroha. Goodbye!")
        print("👋 Aroha assistant shutting down...")
        print("="*60 + "\n")
        self.is_running = False


def main():
    """
    Main entry point for the Aroha voice assistant.
    """
    try:
        assistant = ArohaAssistant()
        assistant.run()
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()