"""
NAME  : bhp_sniffer2.py
AUTHOR: Alexandre Fukaya
DATE  : 03/06/2022

DESCRIPTION:
Raw socket sniffer. It reads a single packet and quit.

    Black Hat Python
    Seitz, Justin
    No Starch Press
    Primeira edição - Dezembro/2014
    isbn:978-15-9327-590-7
    
DEPENDENCIES:
    socket
    os
"""

import socket
import os

host = "192.168.0.196"

if os.name == "nt":
    socket_protocol = socket.IPPROTO_IP
else:
    socket_protocol = socket.IPPROTO_ICMP
sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
sniffer.bind((host, 0))
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

print sniffer.recvfrom(65565)

if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)