# ALL MODULES USED
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys

# INITIALIZING THINGY
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)

# ALL FUNCTIONS~~
# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# to convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said: {query}")

    except Exception as e:
        speak("Say again please...")
        return "none"
    return query

# to greet user
def greet():
    hr = int(datetime.datetime.now().hour)

    if 0 <= hr <= 12:
        speak("Good morning WOO!")
    elif 12 < hr < 18:
        speak("Good afternoon Sir!")
    else:
        speak("Good evening sir...")
    speak("So tell me how can I help ahan?")

# to send email
def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('lakshyaraikwal123@gmail.com', 'lakshya123')
    server.sendmail('lakshyaraikwal85@gmail.com', to, content)
    server.close()

# AHAHAHA SOMETHING IDK~~
if __name__ == "__main__":
    speak("Jarvis activated...")
    greet()

    # ALL COMMANDS LIST
    """
    open vscode
    open google
    open minecraft
    open zoom
    open cmd
    open camera
    open spotify
    get ip address
    open wikipedia
    open youtube
    sending msgs
    playing songs on yt
    sending email
    
    ~can add more but no ideas :))
    """

    while True:
        query = takecommand().lower()

        # Logic building for tasks

        if "open vs code" in query:
            vpath = "C:\\Users\\Lakshya\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vpath)

        elif "open google" in query:
            speak("What should I search on google?")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "open minecraft" in query:
            mpath = "C:\\Program Files (x86)\\Minecraft Launcher\\MinecraftLauncher.exe"
            os.startfile(mpath)

        elif "open zoom" in query:
            zpath = "C:\\Users\\Lakshya\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(zpath)

        elif "open cmd" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow("Camera", img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "open spotify" in query:
            spath = "C:\\Users\\Lakshya\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(spath)

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")

        elif "wikipedia" in query:
            speak("Searching wiki...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wiki")
            speak(result)
            # print(result)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "send message" in query:
            kit.sendwhatmsg("+6591590044", "test message", 20, 43)

        elif "play song" in query:
            kit.playonyt("Fed Up Bazanji")

        elif "send email" in query:
            try:
                speak("what should I say?")
                content = takecommand().lower()
                to = "lakshyaraikwal85@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")

            except Exception as e:
                print(e)
                speak("Sorry sir, an error occurred!")

        elif "no thanks" in query:
            speak("Okay sir...woosh")
            sys.exit()

        speak("Sir, Do you have any other work?")
