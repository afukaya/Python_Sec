#! /usr/bin/python3
# -*- coding: utf-8 -*-

"""
NAME  : bhp_udpclient.py
AUTHOR: Alexandre Fukaya
DATE  : 20/04/2021

DESCRIPTION:
    Provides basic udp server capabilities. This code was adpted to python 3 
    from Black Hat Python book.
    
DEPENDENCIES:
	sockets
    threading

TODO:
       
"""

import socket


target_host = "192.168.0.12"
target_port = 53

s = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
s.sendto(b"d:Data,Data",(target_host,target_port))
data,addr = s.recvfrom(4096)
print(data)