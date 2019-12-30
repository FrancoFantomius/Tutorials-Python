#import pyttsx3
#import os
#engine = pyttsx3.init()
#engine.say("Your Text")
#engine.runAndWait()


import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
speak.Speak("This is the pc voice speaking")
