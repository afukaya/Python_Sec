
def str2bin(ip_address):
    octets = ip_address.split(sep = '.')
    ip_bin = ''
    for octet in octets:
        octet_bin = bin(int(octet)).lstrip('0b').zfill(8)
        ip_bin = ip_bin + octet_bin
    
    return ip_bin

def bin2int(ip_address):
    
    return int(ip_address,2)

def main():
    ip_address = "192.168.1.1"
    print(str2bin(ip_address))

if __name__ == "__main__":
    main()