
def speak(text):
    import pyttsx3
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 180)
    engine.setProperty('volume', 1.0)

    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    del engine
