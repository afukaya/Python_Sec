import socket

target_host = "www.google.com"
target_port = 80

s = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
s.connect((target_host,target_port))
s.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
response = s.recv(4096)
print(response)