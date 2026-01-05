from services.open_application import open_action
from services.wikipedia_ser import search_wikipedia
from services.date_time import tell_time_and_date
from services.weather_ser import get_weather
from speech.recognizer import listen
from speech.speaker import speak
import webbrowser
import random 

stop_messages_hinglish = [ "Assistant band ho raha hai, phir milte hain!",
                           "Main ab sign off kar raha hoon, apna khayal rakho.", 
                           "Bas abhi ke liye itna hi — next time milte hain!", 
                           "Assistant pause ho gaya hai, jab chaaho dobara start kar lena.", 
                           "Session khatam hua, aapko din ki shubhkamnayein!" ]

def handle_command(user_input):
    command = user_input.lower()

    if 'weather' in command:
        if 'in' in command:
            city = command.split('in')[-1].strip() # extract the city name 
            get_weather(city)
        else:
            speak("Which city should I check the weather for?")
            city = listen()
            if city:
                get_weather(city)

    elif any(phrase in command for phrase in ['time', 'date', 'today', 'yesterday']):
         tell_time_and_date(command)

    elif any(phrase in command for phrase in ['who is', 'what is', 'wikipedia']):
            search_wikipedia(command)

    elif 'open' in command:
        open_action(command)

    elif 'search for' in command and 'open' not in command:
        search_query = command.replace("search for", "").strip()
        speak(f"Searching Google for {search_query}")
        webbrowser.open(f"https://www.google.com/search?q={search_query}")

    elif command in ["exit", "quit", "stop"]: 
        msg = random.choice(stop_messages_hinglish) 
        speak(msg)
        return False
    
    return True
