#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
NAME  : bhp_tcpserver.py
AUTHOR: Alexandre Fukaya
DATE  : 20/04/2021

DESCRIPTION:
    Provides basic multithread TCP server capabilities. Usefull when you have no 
    tools for transfering files on a explored asset. This code was adapted to
    python 3 from Black Hat Python book.
    
DEPENDENCIES:
	sockets
    threading

TODO:
       
"""

import socket
import threading

def serverd():
    bind_ip = '0.0.0.0'
    bind_port = '80'
    s = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
    s.bind((bind_ip,bind_port))
    s.listen(10)
    print('Listening on {}:{}'.format(bind_ip,bind_port))
    return s

def handler(s):
    r = s.recv(1024)
    print(' - Received {}'.format(r))
    r.send('Ok!')
    r.close()

s = serverd()

while(True):
    client_socket,client_addr = s.accept()
    print(' - Connection from: {}:{}'.format(client_addr[0],client_addr[1]))
    client_handler = threading.Thread(target=handler,args=(client_socket,))
    client_handler.start()