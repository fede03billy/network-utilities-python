#!/usr/bin/python3

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = socket.gethostname()
host = "192.168.1.54"
port = 444

clientsocket.connect((host, port))

message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))