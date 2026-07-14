import speech_recognition as sr

def test_mic():
    print("Testing Microphone...")
    try:
        devices = sr.Microphone.list_microphone_names()
        print("Available Devices:")
        for i, name in enumerate(devices):
            print(f"Device {i}: {name}")
    except Exception as e:
        print(f"Failed to list devices: {e}")

    try:
        with sr.Microphone() as source:
            print("Microphone successfully opened (Default).")
    except Exception as e:
        print(f"Failed to open default microphone: {e}")

if __name__ == "__main__":
    test_mic()
