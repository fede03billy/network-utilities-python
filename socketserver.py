#!/usr/bin/python3

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host = socket.gethostname()
host = "192.168.1.54"
print(host)
port = 444

serversocket.bind((host, port))

serversocket.listen()

while True:
    clientsocket, address = serversocket.accept()
    print("Ricevo una connessione da %r" % str(address))

    message = "Test OK" + "/r/n"
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()
