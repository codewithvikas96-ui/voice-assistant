import wikipedia
from speech.speaker import speak

def search_wikipedia(query):

    topic = query.replace("search wikipedia for", "").replace("who is", "").replace("what is", "").strip()
    
    speak(f"Searching Wikipedia for {topic}...")
    try:
    
        summary = wikipedia.summary(topic, sentences=2)
        speak("According to Wikipedia:")
        speak(summary)

    except wikipedia.exceptions.DisambiguationError as e:
        speak("That topic is too broad. Please be more specific.")

    except wikipedia.exceptions.PageError:
        speak("I couldn't find any page matching that topic.")
        
    except Exception:
        speak("I'm having trouble connecting to Wikipedia.")