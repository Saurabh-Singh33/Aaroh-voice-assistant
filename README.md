# 🎤 Aroha Voice Assistant

A professional, modular Python voice assistant with speech recognition, text-to-speech, and 13+ powerful features.

## 📋 Features

### Core Functionality

- **🎙️ Wake Word Detection** - Responds to "Hey Aroha" and "Aroha"
- **🗣️ Speech Recognition** - Converts voice to text using Google's API
- **🔊 Text-to-Speech** - Natural voice responses using pyttsx3
- **⚙️ Modular Architecture** - Clean, professional code structure

### Integrated Features

#### 🕐 Time & Date

- Tell current time
- Tell current date

#### 🔍 Search & Information

- Google Search
- Wikipedia Search with summary reading

#### 🌐 Website Management

- Open YouTube, Google, GitHub, Gmail, LinkedIn, and more
- Customizable website list in `data/websites.json`

#### 💻 Application Launcher

- Launch Chrome, VS Code, Notepad, Calculator, Paint, etc.
- Customizable app list in `data/apps.json`

#### 🎵 Media & Entertainment

- Play random music from a folder
- System commands for system control

#### 📊 Productivity Tools
 
- Weather information from OpenWeatherMap API
- System control (shutdown, restart, sleep, lock)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Microphone (for speech recognition)
- Speaker (for audio feedback)

### Installation

1. **Navigate to project directory**

```bash
cd D:\Aaroh-voice-assistant
```

2. **Create a virtual environment** 



3. **Install dependencies**

```bash
pip install -r requirements.txt
```

### Running the Assistant

```bash
python main.py
```

---

## 📁 Project Structure

```
Aaroh-voice-assistant/
│
├── main.py                 # Entry point - Main assistant loop
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── README.md             # This file
│
├── assistant/            # Core assistant modules
│   ├── __init__.py
│   ├── speak.py         # Text-to-speech
│   ├── listen.py        # Speech recognition
│   ├── wake_word.py     # Wake word detection
│   ├── commands.py      # Command processor & router
│   └── utils.py         # Utility functions
│
├── features/            # Feature modules
│   ├── __init__.py
│   ├── date_time.py     # Date and time queries
│   ├── google_search.py # Google search integration
│   ├── wikipedia_search.py # Wikipedia queries
│   ├── open_websites.py # Website launcher
│   ├── open_apps.py     # Application launcher
│   ├── weather.py       # Weather information
│   ├── calculator.py    # Calculator
│   ├── music.py         # Music player
│   └── system_control.py # PC control (shutdown, etc.)
│
├── data/                # Configuration files
│   ├── apps.json        # Application definitions
│   └── websites.json    # Website URLs
│
└── assets/              # Placeholder for assets
```

---

## 💬 Usage Examples

### Time & Date

- "What time is it?"
- "What's today's date?"

### Search

- "Search machine learning"
- "Who is Alan Turing?"

### Open Websites

- "Open YouTube"
- "Go to GitHub"
- "Visit Gmail"

### Open Applications

- "Open VS Code"
- "Launch Chrome"
- "Open Notepad"

### Calculator

- "15 plus 22"
- "100 divided by 5"
- "Calculate 45 \* 3"

### Weather

- "What's the weather in Delhi?"
- "Weather in New York"

### Music

- "Play music"

### System Control

- "Shutdown"
- "Restart"
- "Sleep"
- "Lock PC"

### Help

- "Help" - Display all available commands
- "Exit" or "Goodbye" - Stop the assistant

---

## ⚙️ Configuration

Edit `config.py` to customize:

### Wake Words

```python
WAKE_WORDS = ["hey aroha", "aroha"]
```

### Speech Recognition

```python
RECOGNIZER_TIMEOUT = 5  # Seconds to listen
RECOGNIZER_PHRASE_TIME_LIMIT = 10  # Max record duration
```

### Text-to-Speech

```python
SPEECH_RATE = 150  # Words per minute
SPEECH_VOLUME = 0.9  # Volume (0.0-1.0)
USE_SPEECH = True  # Enable/disable audio
```

### Music Folder

```python
MUSIC_FOLDER = "C:/Users/YourName/Music"  # Set your music folder
SUPPORTED_AUDIO_FORMATS = [".mp3", ".wav", ".flac", ".ogg"]
```

### Feature Flags

```python
ENABLE_WIKIPEDIA = True
ENABLE_WEATHER = True
ENABLE_CALCULATOR = True
ENABLE_MUSIC = True
ENABLE_SYSTEM_CONTROL = True
```

---

## 📝 Customization

### Add Custom Applications

Edit `data/apps.json`:

```json
{
  "applications": {
    "MyApp": "C:\\Path\\To\\App.exe"
  }
}
```

### Add Custom Websites

Edit `data/websites.json`:

```json
{
  "websites": {
    "MyWebsite": "https://www.example.com"
  }
}
```

---

## 🛠️ Technologies Used

- **Python 3.8+**
- **SpeechRecognition** - Voice-to-text
- **pyttsx3** - Text-to-speech
- **Wikipedia** - Wikipedia queries
- **Requests** - HTTP requests for weather API
- **WebbrowserModule** - Opening URLs
- **OS/Subprocess** - System commands

---

## 🌦️ Weather API

Uses **OpenWeatherMap** free API:

- API Key: `4d8fb5b93d4af21d66a2948710284366`
- Get temperature, weather condition, humidity, wind speed

To use your own API key:

1. Sign up at https://openweathermap.org/api
2. Update `WEATHER_API_KEY` in `config.py`

---

## 🐛 Troubleshooting

### Microphone Issues

- Ensure microphone is connected and enabled
- Check Windows audio settings
- Run with `DEBUG_MODE = True` in config.py

### Sound Issues

- Check speaker volume
- Disable `USE_SPEECH = False` in config.py to test without TTS

### App/Website Not Opening

- Verify correct paths in `data/apps.json`
- Check if application is installed
- Use `DEBUG_MODE = True` for error details

### API Errors

- Check internet connection
- Verify API keys in config.py
- Check request timeouts

---

## 📖 Code Style

- **PEP 8** compliant
- **Docstrings** for all functions
- **Error handling** throughout
- **Modular design** - Each feature in separate file
- **Configuration-driven** - Easy customization

---

## 🚀 Future Enhancements

- Voice-based confirmation for system commands
- Machine learning for better command recognition
- Multi-language support
- Local offline recognition
- Smart home integration
- Email and calendar integration
- Custom voice training

---

## 📄 License

This project is open source and available for personal and educational use.

---

## 👨‍💻 Author

Created as a professional Python voice assistant project.

---

## 🤝 Contributing

Feel free to modify and extend the assistant for your needs!

---

## ⚡ Quick Start Command

```bash
python main.py
```

Then say: **"Hey Aroha"** to activate and enjoy!

---

**Enjoy using Aroha! 🎉**
