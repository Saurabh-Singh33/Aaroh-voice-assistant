import webbrowser

while True:
    command = input("You: ").lower()

    if command == "open youtube":
        webbrowser.open("https://www.youtube.com")

    elif command == "open google":
        webbrowser.open("https://www.google.com")

    elif command == "exit":
        print("Bye!")
        break

    else:
        print("Command not found.")