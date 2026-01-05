import speech_recognition as sr
from speech.speaker import speak

def listen():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 300 
    
    with sr.Microphone() as source:
        print("\nListening....")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
            print("Processing voice...")
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        
        except sr.UnknownValueError:
            speak("Sorry, I didn’t catch that.")
            return None
    
        except Exception:
            speak("Sorry, I couldn’t process that request.")
            return None
