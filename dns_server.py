import socket

local_IP = '0.0.0.0'
local_port = 53

s = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
s.bind((local_IP,local_port))
print('Server Running')

while  (True):
    udp_message = s.recvfrom(4096)
    src_message = udp_message[0]
    src_address = udp_message[1]
    print('Recv from {}: {}'.format(src_address,src_message))

    if src_message.startswith(b'd:'):
        print('Data received...')    
        s.sendto(b'Ok',src_address)
    else:
        print('No data received...')
        s.sendto(b'Er',src_address)