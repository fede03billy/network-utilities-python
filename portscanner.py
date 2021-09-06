#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("Insert the IP to scan: ")
port = int(input("Insert the port to scan: "))

print("You are inspecting ", host, " on port ", port)


def portScanner(port):
    if s.connect_ex((host, port)):
        print("The port is closed")
    else:
        print("The port is open")


portScanner(port)
