# Aaroh-voice-assistant

A simple Python voice assistant (Aaroh) that listens for voice or typed commands, opens websites, reports the time, and speaks responses.

Features

- Voice command recognition (microphone)
- Text-to-speech responses (pyttsx3)
- Fuzzy command matching and typed fallback
- Web search and quick website open commands

Quickstart

1. Clone the repository:

   git clone https://github.com/Saurabh-Singh33/Aaroha-voice-assistant.git

2. Install dependencies:

   pip install -r requirements.txt

   Note: On Windows `pyaudio` can be hard to build from source. If installation fails, try `pip install pipwin` followed by:

   pipwin install pyaudio

3. Run the assistant:

   python main.py

Usage

- Say or type commands such as: "open youtube", "open google", "time", "search pizza recipes", "hello", or "exit".
- If microphone or speech libraries are unavailable, the assistant falls back to typed input.

Files

- `main.py`: updated entrypoint with speech I/O, fuzzy matching, and error handling.
- `requirements.txt`: dependency list.

Future improvements

- Add modular assistant packages (listener/speaker/commands)
- Add richer intent handling and integrations (calendar, email, smart home)
- Add tests and CI
