# -*- coding: utf-8 -*-
# versao: v1 - 20/09/2020
import serial
import requests
import os
from gtts import gTTS


def speak(text):
    tts = gTTS(text=text, lang='pt-br')
    tts.save('feedback.mp3')
    os.system('mpg321 feedback.mp3')

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
        strCode = code.decode('utf-8').rstrip('\r')
        print('Codigo detectado, valor: ', strCode)
        payload = {'cpf' : strCode}
        r = requests.post('http://192.168.100.43:3000/', data=payload)
        if len(r.text) < 1:
            feedback = 'Ops, houve um erro, dirija-se ao balcão'
        else:
            feedback = r.text + ', sua entrada foi registrada, você será chamado pelo nome na sala de espera'
        speak(feedback)
