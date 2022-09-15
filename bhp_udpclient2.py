#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
NAME  : bhp_udpclient2.py
AUTHOR: Alexandre Fukaya
DATE  : 20/04/2021

DESCRIPTION:
    Provides basic UDP client functionalities. This code was copied from Black 
    Hat Python book and was written in python 2.7
    
DEPENDENCIES:
	sockets

TODO:
        
"""

import socket

target_address = "127.0.0.1"
target_port = 80

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.sendto("PING",(target_address,target_port))
data,addr = client.recvfrom(4096)
print data