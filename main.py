import webbrowser

while True:
    command = input("You: ").lower()

    if command == "open youtube":
        webbrowser.open("https://www.youtube.com")

    elif command == "open google":
        webbrowser.open("https://www.google.com")

    elif command == "open leetcode":
        webbrowser.open("https://www.leetcode.com")

    elif command == "open github":
        webbrowser.open("https://www.github.com")
        
        elif command == "open google":
        webbrowser.open("https://www.leetcode.com")

    elif command == "open google":
        webbrowser.open("https://www.github.com")




    elif command == "exit":
        print("Bye!")
        break

    else:
        print("Command not found.")
