# 🤖 J.A.R.V.I.S A.I Speech Assistant

A voice-activated desktop assistant inspired by JARVIS from Iron Man. Built in Python and powered by OpenAI GPT-3, it listens, speaks, chats, opens websites, and more.

🎥 Demo Video: https://youtu.be/Z3ZAJoi4x6Q

---

## 🔧 Features
- Voice recognition using `speech_recognition`
- Text-to-speech response (macOS `say` command)
- Chat using GPT-3.5 (`Turbo`)
- Opens common websites (YouTube, Google, Wikipedia)
- Tells the time, plays music, launches apps
- Saves AI-generated content to files

---

## 🚀 Setup

1. Clone the repository  
   `git clone https://github.com/yourusername/jarvis-ai-assistant.git`

2. Install dependencies  
   `pip install speechrecognition openai numpy`

3. Create a `config.py` file with your API key:  
   `apikey = "your-openai-api-key"`

4. Run:  
   `python jarvis.py`

---

## ✨ Sample Commands
- "Open YouTube"
- "What's the time?"
- "Using artificial intelligence, explain black holes"
- "Jarvis Quit"
- "Reset chat"

---

## 📌 Notes
- Designed for macOS (due to `say` and `open`)
- Adjust paths for music or applications if needed

---

## 🧑‍💻 Made by 
@vaishcodescape and @sam5506

MIT License
