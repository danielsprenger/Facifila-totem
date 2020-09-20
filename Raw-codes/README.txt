login e senha do ssh foi deixado como default {pi: raspberry}. Quando for feita a integração com o servidor oficial troque pfvr.

O main.py abre uma porta USB virtual para se comunicar com o leitor, quando é lido um código é feito um post HTTP contendo o valor do código lido.
Para esse script rodar na inicialização usamos o crontab:
Entre no crontab através do comando "sudo crontab -e"
na última linha do documento adicione a seguinte linha "@reboot python /home/pi/Desktop/main.py"
A keyword @reboot diz para o OS que esse script deve ser rodado depois do boot da rPi

o gtts precisa de python 3 para funcionar, a raspberry os utiliza o python 2, então é necessário baixar o python3 e seta-lo como default.

O autofalante usb precisa ser configurado, use os dois links como referencia:
https://computers.tutsplus.com/articles/using-a-usb-audio-device-with-a-raspberry-pi--mac-55876
https://raspberrypi.stackexchange.com/questions/39187/alsa-base-conf-file-missing
O volume do autofalante pode ser ajustado com o alsamixer