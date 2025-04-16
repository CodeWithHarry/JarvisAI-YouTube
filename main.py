# J.A.R.V.I.S A.I Speech Assistant
import speech_recognition as sr
import os
import webbrowser
import openai
from config import apikey
import datetime
import pygame
import threading

# Initialize pygame mixer
try:
    pygame.mixer.init()
except Exception as e:
    print(f"Error initializing pygame mixer: {e}")

chatStr = ""
is_listening = True  # Global flag to control listening

def say(text):
    """Uses the system's text-to-speech functionality."""
    try:
        os.system(f'say "{text}"')
    except Exception as e:
        print(f"Error in say function: {e}")

def takeCommand():
    """Listens to the user's voice command and converts it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Listening...")
            audio = recognizer.listen(source)
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            say("Sorry, I did not understand that.")
            return "Sorry, I did not understand that."
        except sr.RequestError as e:
            say("Sorry, there was an issue with the speech recognition service.")
            print(f"Speech recognition error: {e}")
            return "Speech recognition error."
        except Exception as e:
            say("An error occurred while taking your command.")
            print(f"Error in takeCommand function: {e}")
            return "Some error occurred."

def playMusic(song_name):
    """Plays the specified music file from the 'music' directory."""
    try:
        music_directory = os.path.join(os.getcwd(), "music")
        song_path = os.path.join(music_directory, song_name)

        if not os.path.exists(song_path):
            raise FileNotFoundError(f"The file {song_name} does not exist in the 'music' directory.")

        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        say("Playing music, sir.")
    except FileNotFoundError as e:
        say("Sorry, the music file was not found.")
        print(f"File not found: {e}")
    except pygame.error as e:
        say("Sorry, I couldn't play the music.")
        print(f"Pygame error: {e}")
    except Exception as e:
        say("An unexpected error occurred while playing music.")
        print(f"Error in playMusic function: {e}")

def stopMusic():
    """Stops the currently playing music."""
    try:
        pygame.mixer.music.stop()
        say("Music stopped, sir.")
    except pygame.error as e:
        say("Sorry, I couldn't stop the music.")
        print(f"Pygame error: {e}")
    except Exception as e:
        say("An unexpected error occurred while stopping music.")
        print(f"Error in stopMusic function: {e}")

def cleanup():
    """Stops the music and performs cleanup before exiting."""
    try:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        print("Cleanup completed. Exiting program.")
    except Exception as e:
        print(f"Error during cleanup: {e}")

def introduceYourself():
    """Introduces J.A.R.V.I.S. to the user."""
    try:
        introduction = (
            "Greetings. I am J.A.R.V.I.S., Just A Rather Very Intelligent System – "
            "your personal AI assistant, designed to simplify tasks, answer queries, "
            "and keep you ahead of the curve. How may I assist you today, Sir?"
        )
        say(introduction)
        print(introduction)
    except Exception as e:
        say("Sorry, I encountered an error while introducing myself.")
        print(f"Error in introduceYourself function: {e}")

def chat(query):
    """Handles chat functionality using OpenAI GPT-3.5 Turbo."""
    global chatStr
    try:
        openai.api_key = apikey
        chat_history = [{"role": "system", "content": "You are J.A.R.V.I.S, a helpful AI assistant."}]
        
         
        for line in chatStr.strip().split('\n'):
            if line.startswith("Sir:"):
                chat_history.append({"role": "user", "content": line.replace("Sir: ", "")})
            elif line.startswith("Jarvis:"):
                chat_history.append({"role": "assistant", "content": line.replace("Jarvis: ", "")})

        chat_history.append({"role": "user", "content": query})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chat_history
        )
        response_text = response["choices"][0]["message"]["content"].strip()
        say(response_text)
        chatStr += f"Sir: {query}\nJarvis: {response_text}\n"
        return response_text
    except Exception as e:
        say("Sorry, I encountered an error while processing your request.")
        print(f"Error in chat function: {e}")
        return "Error occurred in chat."
    
def ai(prompt):
    try:
        openai.api_key = apikey
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are J.A.R.V.I.S, a helpful AI assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        text = response["choices"][0]["message"]["content"].strip()

        # Speak and print the response
        say(text)
        print("JARVIS:", text)

        # Save to file safely
        filename = "".join(c if c.isalnum() or c in (' ', '_') else '_' for c in prompt[:50])
        if not os.path.exists("Openai"):
            os.mkdir("Openai")
        with open(f"Openai/{filename}.txt", "w", encoding="utf-8") as f:
            f.write(text)
    except Exception as e:
        say("Sorry, I encountered an error while processing your AI request.")
        print(f"Error in ai function: {e}")
        print(f"Prompt was: {prompt}")

def listenForCommands():
    """Continuously listens for commands in a separate thread."""
    global is_listening
    while True:
        if is_listening:
            query = takeCommand()

            if "play music" in query.lower():
                playMusic("back_in_black_intro.mp3")
            elif "stop music" in query.lower():
                stopMusic()
            elif "introduce yourself" in query.lower():
                introduceYourself()
            elif "the time" in query.lower():
                try:
                    now = datetime.datetime.now()
                    say(f"Sir, the time is {now.strftime('%H')} hours and {now.strftime('%M')} minutes.")
                except Exception as e:
                    say("Sorry, I couldn't fetch the time.")
                    print(f"Error fetching time: {e}")
            elif "open facetime" in query.lower():
                os.system("open /System/Applications/FaceTime.app")
            elif "open pass" in query.lower():
                os.system("open /Applications/Passky.app")
            elif "using artificial intelligence" in query.lower():
                ai(prompt=query)
            elif "jarvis quit" in query.lower():
                say("Goodbye, Sir.")
                cleanup()
                exit()
            elif "reset chat" in query.lower():
                global chatStr
                chatStr = ""
                say("Chat history has been reset.")
            else:
                chat(query)

if __name__ == '__main__':
    try:
        print('Welcome to Jarvis A.I')
        say("Hello Sir, I am Jarvis. How can I help you today?")
        threading.Thread(target=listenForCommands, daemon=True).start()
        while True:
            pass
    except KeyboardInterrupt:
        say("Goodbye, Sir.")
        cleanup()
        print("Exiting Jarvis A.I.")
    except Exception as e:
        say("An unexpected error occurred. Exiting now.")
        cleanup()
        print(f"Unexpected error in main loop: {e}")