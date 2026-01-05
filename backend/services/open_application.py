import webbrowser
import os
import platform
from speech.speaker import speak

def open_action(command):

    if 'google' in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
        
    elif 'youtube' in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
        
    elif 'github' in command:
        speak("Opening GitHub")
        webbrowser.open("https://www.github.com")

    elif 'notepad' in command:
        speak("Opening Notepad")
        os.system("notepad") 
        
    elif 'linkedin' in command:
        speak("Opening Linkedin")
        webbrowser.open("https://linkedin.com")

    elif 'calculator' in command:
        speak("Opening Calculator")
        if platform.system() == "Windows":
            os.system("calc")
        else:
            os.system('open -a Calculator')

    else:
        speak("Unable to open")