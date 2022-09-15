#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
NAME  : bhp_tcpserver2.py
AUTHOR: Alexandre Fukaya
DATE  : 20/04/2021

DESCRIPTION:
    Provides basic multithread TCP server capabilities. Usefull when you have no 
    tools for transfering files on a explored asset. This code was copied from 
    Black Hat Python book and was written in python 2.7
    
DEPENDENCIES:
	sockets
    threading

TODO:
       
"""

import socket
import threading

bind_address = "0.0.0.0"
bind_port    = 3333

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print "[*] Received: %s" % request
    client_socket.send("ACK!")
    client_socket.close()

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((bind_address,bind_port))
server.listen(5)
print "[*] Listening on %s:%d" % (bind_address,bind_port)

while True:
    client,addr = server.accept()
    print "[*] Accepted connection from: %s:%d" % (addr[0],addr[1])
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()