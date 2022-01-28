import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import random
from PIL import ImageGrab
import pyautogui
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # getting details of current voice
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        p = "Good morning!"
    elif hour >= 12 and hour < 18:
        p = "Good afternoon!"
    else:
        p = "Good evening!"

    p = p + " I am Nemo. Please tell me how I may help you."
    print(f"Nemo : {p}")
    speak(p)


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.7
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f"User : {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        print("Say that again please...")  # Say that again will be printed in case of improper voice
        return "None"  # None string will be returned

    return query

def main():

    wishme()
    while True:
        query = takeCommand().lower()

        if 'search' in query:
            try:
                speak('Searching Wikipedia..')
                query = query.replace("search", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(f"Nemo : According to Wikipedia, {results}")
                speak(results)
            except Exception as e:
                p = "Sorry no results found"
                print(f"Nemo : {p}")
                speak(p)

        elif 'open youtube' in query:
            webbrowser.open("Youtube.com")

        elif 'open google' in query:
            webbrowser.open("Google.com")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            p = f"The time is {strTime}"
            print(f"Nemo : {p}")
            speak(p)

        elif 'play music' in query:
            music_dir = 'C:\\Users\\gosai\\Music'
            songs = os.listdir(music_dir)
            i = random.randint(0, len(songs) - 1)
            os.startfile(os.path.join(music_dir, songs[i]))

        elif 'play movie' in query:
            movie_dir = 'C:\\Users\\gosai\\Videos\\Movies'
            movie = os.listdir(movie_dir)
            i = random.randint(0, len(movie) - 1)
            os.startfile(os.path.join(movie_dir, movie[i]))

        elif 'screenshot' in query:
            image = ImageGrab.grab()  # take screenshot
            image.show()  # show taken screenshot

        elif 'record screen' in query:
            pyautogui.hotkey('win', 'alt', 'r')

        elif 'stop screen recording' in query:
            pyautogui.hotkey('win', 'alt', 'r')

        elif 'open chrome' in query:
            path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
            os.startfile(os.path.join(path))

        elif 'open game' in query:
            path = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Riot Games\VALORANT.lnk'
            os.startfile(os.path.join(path))

        elif 'open notepad' in query:
            path = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Notepad.lnk'
            os.startfile(os.path.join(path))


if __name__ == "__main__":

    main()
