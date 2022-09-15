#! /usr/bin/python3
# -*- coding: utf-8 -*-

"""
NAME  : dns_client.py
AUTHOR: Alexandre Fukaya
DATE  : 13/08/2020

DESCRIPTION:
    Provides basic DNS query functionalities. 
    
DEPENDENCIES:
	sockets

TODO:
        
"""

import socket

target_host = "192.168.0.12"
target_port = 53

s = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
s.sendto(b"d:Data,Data",(target_host,target_port))
data,addr = s.recvfrom(4096)
print(data)