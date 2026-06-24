import random
import webbrowser
from datetime import datetime

try:
    import speech_recognition as sr
except Exception:
    sr = None

try:
    import pyttsx3
    engine = pyttsx3.init()
except Exception:
    engine = None

COMMAND_LINKS = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "github": "https://github.com",
    "stackoverflow": "https://stackoverflow.com",
    "news": "https://news.google.com",
}

JOKES = [
    "Why did the programmer quit his job? Because he didn't get arrays.",
    "Why do Java developers wear glasses? Because they can't C#.",
    "I would tell you a UDP joke, but you might not get it.",
    "Why did the computer show up at work late? It had a hard drive.",
]

RESPONSES = {
    "greeting": [
        "Hello! How can I help you today?",
        "Hi there! What would you like to do?",
    ],
    "unknown": [
        "Sorry, I don't know that command. Say help to see what I can do.",
        "I couldn't understand that. Try asking for help.",
    ],
}


def speak(text):
    print("Assistant:", text)
    if engine:
        engine.say(text)
        engine.runAndWait()


def listen():
    if sr:
        try:
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source)
            return recognizer.recognize_google(audio).lower()
        except Exception:
            speak("I couldn't understand your voice, please type your command.")

    return input("You: ").strip().lower()


def show_help():
    speak("Here are the commands I understand:")
    for phrase in [
        "hello / hi",
        "time",
        "date",
        "search <query>",
        "open <site>",
        "youtube",
        "google",
        "github",
        "stackoverflow",
        "news",
        "wikipedia <topic>",
        "joke",
        "help",
        "exit / quit / bye",
    ]:
        print(" -", phrase)


def open_link(command):
    for name, url in COMMAND_LINKS.items():
        if name in command:
            speak(f"Opening {name.title()}")
            webbrowser.open(url)
            return True
    return False


def search_google(command):
    if command.startswith("search"):
        query = command.replace("search", "", 1).strip()
        if query:
            speak(f"Searching Google for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query.replace(' ', '+')}")
        else:
            speak("What should I search for?")
        return True
    return False


def search_wikipedia(command):
    if command.startswith("wikipedia"):
        query = command.replace("wikipedia", "", 1).strip()
        if query:
            speak(f"Searching Wikipedia for {query}")
            webbrowser.open(f"https://en.wikipedia.org/wiki/{query.replace(' ', '_')}")
        else:
            speak("Which Wikipedia topic would you like?")
        return True
    return False


def main():
    speak("Aaroh Assistant started. Say help to see my commands.")

    while True:
        command = listen()

        if "youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "time" in command:
            current = datetime.now().strftime("%H:%M")
            speak(f"The time is {current}")

        elif command.startswith("search"):
            query = command.replace("search", "").strip()
            if query:
                speak(f"Searching {query}")
                webbrowser.open(
                    f"https://www.google.com/search?q={query.replace(' ', '+')}"
                )
            else:
                speak("What should I search?")

        elif command in ["exit", "quit", "bye"]:
            speak("Goodbye")
            break

        elif "hello" in command or "hi" in command:
            speak("Hello! How can I help you?")

        else:
            speak("Sorry, I don't know that command.")


if __name__ == "__main__":
    main()