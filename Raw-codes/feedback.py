import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTs

def speak(text):
    tts = gTTs(text=text, lang='pt-br')
    filename= "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

speak("Bom dia Facifila")
