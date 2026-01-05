import requests
from speech.speaker import speak
from config import WEATHER_API_KEY


def get_weather(city):

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
  
        if data["cod"] == 200:
            main = data["main"]
            weather_desc = data["weather"][0]["description"]
            temp = main["temp"]
            feels_like = main["feels_like"]
            
            report = f"In {city}, it is currently {temp} degrees Celsius with {weather_desc}. It feels like {feels_like} degrees."
            speak(report)
        else:
            speak(f"I couldn't find weather information for {city}. Please check the spelling.")
            
    except Exception:
        speak("I'm having trouble connecting to the weather service right now.")