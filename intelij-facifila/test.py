# -*- coding: utf-8 -*-
# versao: v0 - 12/09/2020
import serial
import requests

clean_code = "109.213.779-32"
payload = {'cpf': clean_code}
r = requests.post('http://192.168.100.43:3000/', data=payload)
print(r.text)
