#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
NAME  : bhp_tcpclient.py
AUTHOR: Alexandre Fukaya
DATE  : 25/01/2019

DESCRIPTION:
    Provides a basic TCP client example using socket library. This code was 
    adpted to python from Black Hat Python book.
    
DEPENDENCIES:
	sockets

TODO:
            
"""

import socket

target_host = "www.google.com"
target_port = 80

s = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
s.connect((target_host,target_port))
s.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
response = s.recv(4096)
print(response)