#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
NAME  : bhp_tcpclient2.py
AUTHOR: Alexandre Fukaya
DATE  : 25/01/2019

DESCRIPTION:
    Provides a basic TCP client example using socket library. This code was 
    copied from Black Hat Python book and was written in Python 2.
    
DEPENDENCIES:
	sockets

TODO:
            
"""

import socket

target_address = "www.google.com"
target_port = 80

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((target_address,target_port))
client.send("GET / HTTP/1.1\r\nHost:google.com\r\n\r\n")
response = client.recv(4096)
print response