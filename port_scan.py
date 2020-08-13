#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
NAME  : port_scan.py
AUTHOR: Alexandre Fukaya
DATE  : 16/11/2018

DESCRIPTION:
    Checks if a given list of ports are open on a target machine.
    
DEPENDENCIES:

"""

from scapy.all import *

conf.verb = 0
ports     = [21,22,23,80,8080]
ip_addr   = '192.168.1.1'
ip_pkt    = IP(dst = ip_addr)
tcp_pkt   = TCP(dport = ports,flags='S')
send_pkt  = ip_pkt / tcp_pkt
ans,unas  = sr(send_pkt,inter=0.1,timeout=1)

print('Port\tState')
for recv_pkt in ans:
    print(recv_pkt[1][IP].sport,'\t',recv_pkt[1][TCP].sprintf('%flags%'))
