from speech.speaker import speak
from datetime import timedelta
import datetime

def tell_time_and_date(query):
    now = datetime.datetime.now()
    
    if 'yesterday' in query:
        yesterday = now - timedelta(days=1)
        date_str = yesterday.strftime("%A, %B %d")
        speak(f"Yesterday was {date_str}")
        
    elif 'time' in query:
        current_time = now.strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
        
    elif 'date' in query or 'today' in query:
        date_str = now.strftime("%A, %B %d, %Y")
        speak(f"Today is {date_str}")
