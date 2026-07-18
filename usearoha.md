# Using Aroha Voice Assistant

Aroha is a versatile, modular voice assistant designed to help you with various daily tasks through simple voice commands. This comprehensive guide will walk you through how to start, interact with, and utilize all the features of your Aroha assistant.

## Getting Started

1. **Start the Assistant**: Run the `main.py` script from your terminal:
   ```bash
   python main.py
   ```
2. **Wake Word**: Once the assistant is running and says "Aroha is ready", simply say **"Hey Aroha"** or **"Aroha"** to get its attention.
3. **Wait for Prompt**: Aroha will reply "I'm listening. What would you like?" and you can speak your command.
   *(Alternatively, you can say the wake word and command together, e.g., "Hey Aroha, what is the weather in London?")*

---

## Detailed Features & Commands

Aroha supports a wide range of modules. Here are detailed examples and requirements for each one:

### 🌤️ Weather App
Get real-time weather updates for any city around the world using the OpenWeatherMap API.
- **How to use**: Say something like:
  - *"Weather in London"*
  - *"What is the weather in New York?"*
  - *"Tell me the weather for Tokyo"*
- **Response**: Aroha will provide the current temperature (in Celsius), weather description (e.g., clear sky, scattered clouds), humidity percentage, and wind speed (in meters per second).
- **Configuration required**: Ensure your `WEATHER_API_KEY` is set correctly in `config.py` (an OpenWeatherMap key). Also ensure you have an active internet connection.

### 🧮 Calculator
Perform simple mathematical calculations on the fly.
- **How to use**: State your mathematical expression clearly:
  - *"Calculate 15 plus 22"*
  - *"What is 100 divided by 5"*
  - *"50 times 4"*
  - *"100 minus 30"*
- **Supported Operations**: Plus (+), Minus (-), Times / Multiplied by (*), Divide / Divided by / Into (/).

### 📅 Date & Time
Ask Aroha for the current system date or time.
- **How to use**: 
  - *"What time is it?"*
  - *"Tell me the time"*
  - *"What is today's date?"*

### 🌐 Web & Wikipedia Search
Search the internet or Wikipedia for quick information.
- **Google Search**: 
  - *"Search Google for Python programming"*
  - *"Google how to bake a cake"*
  - (This will open your default browser with the Google search results)
- **Wikipedia Search**: 
  - *"Search Wikipedia for Albert Einstein"*
  - *"Who is Nikola Tesla on Wikipedia"*
  - (Aroha will read a brief 2-sentence summary of the Wikipedia article out loud).

### 💻 System Control & Apps
Control your computer or open applications and websites.
- **Open Websites**: 
  - *"Open YouTube"*
  - *"Open Google"*
  - *"Visit GitHub"*
  - (You can add custom websites in `data/websites.json`)
- **Open Applications**: 
  - *"Open Notepad"*
  - *"Open Calculator"* (opens Windows system calculator)
  - *"Launch Chrome"*
  - (You can map new application names to their `.exe` paths in `data/apps.json`)
- **System Control**: 
  - *"Shutdown"* or *"Turn off computer"*
  - *"Restart PC"*
  - *"Sleep"*
  - *"Lock PC"*

### 🎵 Music & Fun
Enjoy some entertainment with Aroha.
- **Music**: 
  - *"Play music"* 
  - (This will play a random audio file from your local music folder. Make sure `MUSIC_FOLDER` is correctly configured in `config.py`).
- **Fun / Conversational**: 
  - *"Tell me a joke"*
  - *"How are you?"*
  - *"Who created you?"*

---

## Configuration (`config.py`)

To get the most out of Aroha, you might need to tweak a few settings in the `config.py` file:
- **`WAKE_WORDS`**: Change what Aroha responds to (default is `["hey aroha", "aroha"]`).
- **`WEATHER_API_KEY`**: Insert your OpenWeatherMap API key here for the weather module to work.
- **`MUSIC_FOLDER`**: Point this to your local music directory (e.g., `C:/Users/YourName/Music`) for the "Play music" command.
- **Feature Toggles**: You can enable or disable specific features (like `ENABLE_WEATHER` or `ENABLE_WIKIPEDIA`) by setting them to `True` or `False`.

---

## Exiting the Assistant

When you are done using Aroha, you can gracefully shut down the assistant by saying any of the following exit commands:
- *"Exit"*
- *"Quit"*
- *"Goodbye"*
- *"Stop listening"*
- *"Bye"*

Aroha will reply "Thank you for using Aroha. Goodbye!" and close the application.
