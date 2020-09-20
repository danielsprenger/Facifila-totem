import playsound
from gtts import gTTS


def speak(text):
    tts = gTTS(text=text, lang='pt-br')
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


speak("Bom dia Facifila")
