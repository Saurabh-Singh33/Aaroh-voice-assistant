import webbrowser
from datetime import datetime

try:
    import speech_recognition as sr
except:
    sr = None

try:
    import pyttsx3
    engine = pyttsx3.init()
except:
    engine = None


def speak(text):
    print("Assistant:", text)
    if engine:
        engine.say(text)
        engine.runAndWait()


def listen():
    if sr:
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source)
            return r.recognize_google(audio).lower()
        except:
            pass

    return input("You: ").lower()


def main():
    speak("Aaroh Assistant Started")

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