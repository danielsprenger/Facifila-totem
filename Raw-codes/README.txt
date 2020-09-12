O main.py abre uma porta USB virtual para se comunicar com o leitor, quando é lido um código é feito um post HTTP contendo o valor do código lido.
Para esse script rodar na inicialização usamos o crontab:
Entre no crontab através do comando "sudo crontab -e"
na última linha do documento adicione a seguinte linha "@reboot python /home/pi/Desktop/main.py"
A keyword @reboot diz para o OS que esse script deve ser rodado depois do boot da rPi