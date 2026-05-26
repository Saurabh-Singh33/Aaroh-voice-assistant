# Aaroh-voice-assistant

A Python-based voice assistant for automation and voice commands.
Aaroha can listen to user commands, perform desktop automation tasks, open applications/websites, and respond using speech.

Features
Voice command recognition
Text-to-speech responses
Open websites and desktop applications
Basic desktop automation
AI integration support (future scope)
Modular and scalable architecture
Offline command support
Tech Stack
Python
speech_recognition
pyttsx3
pyautogui
webbrowser
os
subprocess
Project Structure
Aaroha-voice-assistant/
│
├── main.py                 # Entry point
├── assistant/
│   ├── listener.py         # Speech recognition
│   ├── speaker.py          # Text-to-speech
│   ├── commands.py         # Command handling
│   └── automation.py       # Automation features
│
├── assets/
│
├── requirements.txt
├── README.md
└── .gitignore
Installation

Clone the repository:

git clone https://github.com/Saurabh-Singh33/Aaroha-voice-assistant.git

Move into the project folder:

cd Aaroha-voice-assistant

Install dependencies:

pip install -r requirements.txt
Run the Project
python main.py
Example Commands
“Open YouTube”
“Open Chrome”
“Search Python tutorials”
“What is the time?”
“Shutdown system”
Future Improvements
AI chatbot integration
Wake word detection
GUI dashboard
Smart home control
Offline NLP model
Multi-language support
