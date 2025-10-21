# import speech_recognition as sr
# import webbrowser
# import pyttsx3

# recognizer = sr.Recognizer()
# engine = pyttsx3.init

# r = recognizer.recognize_google()

import speech_recognition as sr
import pyttsx3
import webbrowser

# Optional: Create a music library as a dictionary
musicLibrary = {
    "shapeofyou": "https://www.youtube.com/watch?v=JGwWNGJdvx8",
    "faded": "https://www.youtube.com/watch?v=60ItHLz5WEA"
    # Add more songs here
}

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    c = c.lower()
    
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif c.startswith("play"):
        try:
            song = c.split(" ", 1)[1]  # Get everything after "play"
            if song in musicLibrary:
                link = musicLibrary[song]
                webbrowser.open(link)
                speak(f"Playing {song}")
            else:
                speak("Sorry, I don't know that song.")
        except IndexError:
            speak("Please say the name of the song after 'play'.")
    else:
        speak("Sorry, I didn't understand that command.")

if __name__ == "__main__":
    speak("Initializing Jarvis......")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)

            word = recognizer.recognize_google(audio)

            if word.lower() == "jarvis":
                speak("How can I help you?")
                with sr.Microphone() as source:
                    print("Jarvis active, listening for command...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

                command = recognizer.recognize_google(audio)
                print("Command:", command)
                processcommand(command)

        except Exception as e:
            print(f"Error: {e}")
