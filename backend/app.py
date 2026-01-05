from speech.speaker import speak
from speech.recognizer import listen
from router.command_route import handle_command


def main():
    speak("Assistant Activated...")
    speak("Hello, I am your voice assistant. How can I help you?")

    running = True 
    while running:
        command = listen()
        if command:
            running = handle_command(command)
    

if __name__ == "__main__":
    main()