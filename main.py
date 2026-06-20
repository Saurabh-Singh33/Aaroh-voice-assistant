import webbrowser

print("=== Aaroh Voice Assistant ===")
print("Available Commands:")
print("- open youtube")
print("- open google")
print("- exit / quit / bye")

while True:
    command = input("\nYou: ").strip().lower()

    if command == "open youtube":
        print("Opening YouTube...")
        webbrowser.open("https://www.youtube.com")

    elif command == "open google":
        print("Opening Google...")
        webbrowser.open("https://www.google.com")

    elif command == "exit":
        print("Bye!")
        break

    else:
        print("Command not found.")