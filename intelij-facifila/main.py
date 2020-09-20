# -*- coding: utf-8 -*-
# versao: v0 - 12/09/2020
import serial
import requests
from gtts import gTTS
import playsound #usa os na rpi


def speak(text):
    tts = gTTS(text=text, lang='pt-br')
    tts.save("feedback.mp3")
    playsound.playsound("feedback.mp3")
    #os.system("mpg321 feedback.mp3")



ser = serial.Serial()
ser.baudrate = 115200
ser.timeout = 1
ser.port = '/dev/ttyACM0'

try:
    ser.open()
except serial.SerialException:
    print('Falha ao conectar com o leitor')
    exit()

while True:
    code = ser.readline()
    if len(code) > 0:
        print('código detectado, valor: ', code)
        size = len(code)
        clean_code = code[:size - 1] #remove o carrier return
        payload = {'cpf': clean_code}
        r = requests.post('http://192.168.100.43:3000/', data=payload)
        if len(r.text) < 1:
            feedback = "Ops, houve algum erro, dirijasse até o balcão"
        else:
            feedback = "Tudo certo " + r.text + ", aguarde ser chamado pelo seu nome"
        speak(feedback)
