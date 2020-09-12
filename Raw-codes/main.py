# -*- coding: utf-8 -*-
# versao: v0 - 12/09/2020
import serial
import requests

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
