

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch('SAPI.spVoice')
    speak.Speak(str)

speak("hello world")


import pyttsx3

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak2(str):
    engine.say(str)
    engine.runAndWait()

speak2("Iam jeevan from J S S Academy of Technical education- Bangalore")