import pyautogui
import playsound
import time
from gtts import gTTS
import speech_recognition as sr
import os

def Startsignal():
    playsound.playsound('Start.wav') #Path to File

def Stopsignal():
    playsound.playsound('End.wav') #Path to File

def Musikstart():
    pyautogui.click(360, 1060) #Spotify location in your Taskbar

def Musikstopresume():
    pyautogui.press("space")

def speak(text):
    tts = gTTS(text=text,lang="en")
    filename = "Voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove("Voice.mp3")

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    return said

ChestBiceps = ["barbell bench press ","barbell Curl ", "dumbbell bench press", "dumbbell butterfly"," shoulder press ","dumbbell bicepscurl ","dumbbell wideswings"] #Enter weight/repititions after each exercise so you can track your progress
BackTriceps = ["barbell deadlift","barbell rowing ","barbell shoulder press","French Press", "Dips", "Skullcrusher" ]
Legs = ["squats", "calf raises","pushups","Leg Raises", "Pistol Squats", "Crunch Cross"]
Slingtrainer = ["chest press", "butterflypress","rowing vertical","rowing horizontal", "butterfly reverse", "Crunches"]
abs = ["Boxbanana","Russian Twist","Hip Raises","Lateral Kicks","Plank Rotation","Toe Touches","Side to side","Plank to Pushup","banana seesaw"]
New = []

Routine = abs #Enter Routine here

Music = input("do you want to play music from spotify? (yes/no):  ")

if Music == "yes":
    speak("Say start to start")
    text = get_audio()
    if "start" or "stop" in text:
        Musikstart()
        time.sleep(3)
        listvar = 0
        for ii in range(50):
                Zahl = 1
                speak(Routine[listvar])
                time.sleep(1)
                speak("Are you ready?")
                text1 = get_audio()
                if "yes" in text1:
                    listvar += 1
                    if Routine != abs:
                        for i in range(3):
                            speak("Round" + str(Zahl))
                            time.sleep(1)
                            Musikstopresume()
                            Startsignal()
                            time.sleep(45)
                            Stopsignal()
                            time.sleep(20)
                            Zahl += 1
                    else:
                        for i in range(1):
                            speak("Round" + str(Zahl))
                            Musikstopresume()
                            time.sleep(1)
                            Startsignal()
                            time.sleep(45)
                            Stopsignal()
                            time.sleep(20)
                            Zahl += 1

                else:
                    continue

elif Music == "no":
    speak("Say start to start")
    text = get_audio()
    if "start" or "stop" in text:
        listvar = 0
        for ii in range(50):
            Zahl = 1
            speak(Routine[listvar])
            time.sleep(1)
            speak("Are you ready?")
            text1 = get_audio()
            if "yes" in text1:
                listvar += 1
                if Routine != abs:
                    for i in range(3):
                        speak("Round" + str(Zahl))
                        time.sleep(1)
                        Startsignal()
                        time.sleep(45)
                        Stopsignal()
                        time.sleep(20)
                        Zahl += 1
                else:
                    for i in range(1):
                        speak("Round" + str(Zahl))
                        time.sleep(1)
                        Startsignal()
                        time.sleep(45)
                        Stopsignal()
                        time.sleep(20)
                        Zahl += 1

            else:
                continue