# 🎙️ Voice Assistant (Python)

## Problem Statement
In today’s fast-paced digital world, users want hands-free, intelligent assistants that can understand natural language and perform daily tasks efficiently—similar to Alexa, Google Assistant, or Siri.

## Solution

This project builds an Advanced Voice Assistant capable of:
- Understanding spoken language
- Interpreting user intent using NLP
- Performing real-world tasks autonomously
- Integrating with third-party APIs for extended functionality

This assistant is designed as a modular, scalable system, not just a basic speech-to-text script.

---

A simple voice assistant built with Python that can: 
- Open applications
- Search Wikipedia
- Fetch weather information
- Tell date and time
- Perform Google searches
- Exit gracefully with Hinglish stop messages

---

## ✨ Features 
- 🎤 **Speech Recognition** - Understands your voice commands using `speech_recognition`.
- 🔊 **Text-to-Speech** – Speaks back responses with `pyttsx3`.
- 🌦️ **Weather Updates** – Get real-time weather for any city.
- 📅 **Date & Time** – Ask for today’s date or current time.
- 🔍 **Google Search** – Search the web instantly.
- 📖 **Wikipedia Search** – Fetch summaries from Wikipedia.
- 🛑 **Graceful Exit** – Hinglish farewell messages when you say *exit/quit/stop*. 

---

## System Architecture
```
User (Voice)
   ↓
Microphone Input
   ↓
Speech Recognition Module
   ↓
Command Router
   ↓
Task Execution Layer
   ├── Date and time
   ├── Open applications
   ├── Weather API
   ├── Wikipedia service
   ├── Google service
   ↓
Text-to-Speech Output
   ↓
User (Voice Response)

```

---

## 🛠️ Tech Stack 
- **Python 3.9+**
- `speech_recognition`
- `pyttsx3`
- `wikipedia`
- `requests`
- `webbrowser`
- `os`
- `platform`

---

## ▶️ Usage
Run the assistant:
```
python app.py
```

Say commands like:
- "Search for Rohit Sharma"
- "Open Notepad"
- "What's the weather in Mumbai?"
- "Tell me the time"
- "Stop"

---

## 🛑 Exit
Say "exit", "quit", or "stop" to end the assistant.
You’ll hear a friendly Hinglish goodbye like:
"Assistant band ho raha hai, phir milte hain!"

---
