import socket


target_host = "192.168.0.12"
target_port = 53

s = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
s.sendto(b"d:Data,Data",(target_host,target_port))
data,addr = s.recvfrom(4096)
print(data)