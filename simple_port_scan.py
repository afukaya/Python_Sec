"""
NAME  : simple_port_scan.py
AUTHOR: Alexandre Fukaya
DATE  : 17/11/2018

DESCRIPTION:
    Checks if a given list of ports are open on a target machine.
    
DEPENDENCIES:

"""

import socket

host  = '192.168.1.1'
ports =  [21,22,23,80]
print('Open Ports')
for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    ret_code = s.connect_ex((host,port))
    s.close()
    if ret_code == 0:
        print(port)
