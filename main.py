import webbrowser
import sys
import logging
from datetime import datetime
from difflib import get_close_matches

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")

try:
    import speech_recognition as sr
except Exception:
    sr = None

try:
    import pyttsx3
except Exception:
    pyttsx3 = None


def speak(text: str):
    if pyttsx3:
        try:
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            logging.warning("TTS failed, falling back to print: %s", e)
            print("Assistant:", text)
    else:
        print("Assistant:", text)


def listen(prompt: str = "You: ") -> str:
    # Prefer microphone if available
    if sr:
        recognizer = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                logging.info("Listening (say something or press Ctrl+C to type)...")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)
            try:
                text = recognizer.recognize_google(audio)
                logging.info("Heard: %s", text)
                return text.lower()
            except sr.UnknownValueError:
                logging.info("Speech not understood")
                return ""
            except sr.RequestError as e:
                logging.warning("Speech service error: %s", e)
                return ""
        except Exception as e:
            logging.info("Microphone not available or error: %s", e)
            # Fall through to typed input

    # Fallback: typed input
    try:
        return input(prompt).strip().lower()
    except KeyboardInterrupt:
        return "exit"


def open_youtube(_=None):
    speak("Opening YouTube")
    webbrowser.open("https://www.youtube.com")


def open_google(_=None):
    speak("Opening Google")
    webbrowser.open("https://www.google.com")


def tell_time(_=None):
    now = datetime.now().strftime("%H:%M")
    speak(f"The time is {now}")


def say_hello(_=None):
    speak("Hello! How can I help you?")


def do_search(query: str):
    if not query:
        speak("What should I search for?")
        return
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    speak(f"Searching for {query}")
    webbrowser.open(url)


def unknown(_=None):
    speak("Sorry, I didn't get that. Try: open youtube, open google, time, search <query>, or exit.")


COMMANDS = {
    "open youtube": open_youtube,
    "open google": open_google,
    "time": tell_time,
    "what time is it": tell_time,
    "hello": say_hello,
    "hi": say_hello,
    "search": do_search,
    "exit": lambda _=None: (_ for _ in ()).throw(SystemExit()),
    "quit": lambda _=None: (_ for _ in ()).throw(SystemExit()),
    "bye": lambda _=None: (_ for _ in ()).throw(SystemExit()),
}


def match_command(text: str):
    if not text:
        return None, None

    # direct startswith matching for commands with arguments like 'search'
    if text.startswith("search "):
        return "search", text[len("search "):]

    # exact match
    if text in COMMANDS:
        return text, None

    # fuzzy match
    choices = list(COMMANDS.keys())
    matches = get_close_matches(text, choices, n=1, cutoff=0.6)
    if matches:
        return matches[0], None

    return None, None


def main():
    speak("Aaroh Voice Assistant started. Say a command or type one.")
    logging.info("Available commands: %s", ", ".join(sorted(set(COMMANDS.keys()))))

    while True:
        try:
            text = listen()
            if not text:
                continue

            cmd, arg = match_command(text)
            if cmd:
                func = COMMANDS.get(cmd, unknown)
                if cmd == "search":
                    func(arg)
                else:
                    func(arg)
            else:
                unknown()

        except SystemExit:
            speak("Goodbye!")
            break
        except Exception as e:
            logging.exception("Error during main loop: %s", e)
            speak("An error occurred. Check logs.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        speak("Interrupted. Bye!")
        sys.exit(0)