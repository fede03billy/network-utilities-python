#!/usr/bit/python3

import socket


def banner(ip, port):
    s = socket.socket()
    s.connect((ip, int(port)))
    print(str(s.recv(1024)).strip('b'))


def main():
    ip = input("Entrer an IP: ")
    port = str(input("Enter a port: "))
    banner(ip, port)


main()
