# Working with Aroha Voice Assistant

Aroha is a versatile voice assistant designed to help you with various daily tasks through simple voice commands. This guide will walk you through how to start, interact with, and utilize all the features of your Aroha assistant.

## Getting Started

1. **Start the Assistant**: Run the `main.py` script from your terminal:
   ```bash
   python main.py
   ```
2. **Wake Word**: Once the assistant is running and says "Aroha is ready", simply say **"Hey Aroha"** to get its attention.
3. **Wait for Prompt**: Aroha will reply "I'm listening. What would you like?" and you can speak your command.
   *(Alternatively, you can say the wake word and command together, e.g., "Hey Aroha, what is the weather in London?")*

## Features and How to Use Them

Aroha supports a wide range of modules. Here are examples of how to interact with each one:

### 🌤️ Weather App
Get real-time weather updates for any city.
- **How to use**: Say something like:
  - *"Weather in London"*
  - *"What is the weather in New York?"*
  - *"Tell me the weather for Tokyo"*
- **Response**: Aroha will provide the current temperature (in Celsius), weather description, humidity, and wind speed.

### 🧮 Calculator
Perform simple mathematical calculations on the fly.
- **How to use**: State your mathematical expression clearly:
  - *"Calculate 15 plus 22"*
  - *"What is 100 divided by 5"*
  - *"50 times 4"*
  - *"100 minus 30"*
- **Supported Operations**: Plus (+), Minus (-), Times / Multiplied by (*), Divide / Divided by / Into (/).

### 📅 Date & Time
Ask Aroha for the current date or time.
- **How to use**: 
  - *"What time is it?"*
  - *"Tell me the time"*
  - *"What is today's date?"*

### 🌐 Web & Wikipedia Search
Search the internet or Wikipedia for quick information.
- **Google Search**: 
  - *"Search Google for Python programming"*
  - *"Google how to bake a cake"*
- **Wikipedia Search**: 
  - *"Search Wikipedia for Albert Einstein"*
  - *"Who is Nikola Tesla on Wikipedia"*

### 💻 System Control & Apps
Control your computer or open applications and websites.
- **Open Websites**: 
  - *"Open YouTube"*
  - *"Open Google"*
- **Open Applications**: 
  - *"Open Notepad"*
  - *"Open Calculator"* (opens system calculator)
- **System Control**: 
  - Commands to adjust volume, mute, or manage system functions (depending on your OS).

### 🎵 Music & Fun
Enjoy some entertainment with Aroha.
- **Music**: 
  - *"Play music"* 
  - *"Play [song name] on YouTube"*
- **Fun**: 
  - Ask Aroha to tell a joke or ask it conversational questions.

## Exiting the Assistant

When you are done using Aroha, you can gracefully shut down the assistant by saying any of the following exit commands:
- *"Exit"*
- *"Quit"*
- *"Goodbye"*
- *"Stop listening"*
- *"Bye"*

Aroha will reply "Thank you for using Aroha. Goodbye!" and close the application.
