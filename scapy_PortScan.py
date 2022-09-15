from scapy.all import *

conf.verb = 0
host = '192.168.0.1'
portas = [22,80,443,12345]
pacote = IP(dst=host)/TCP(dport=portas,flags='S')
ans,uans = sr(pacote,inter=0.1,timeout=1)

print('Porta \t Estado')

for pacoteRecebido in ans:
    if pacoteRecebido[1].haslayer('ICMP'):
        if pacoteRecebido[1]['ICMP'].type == 3 and pacoteRecebido[1]['ICMP'].code == 3:
            print('{} \t Rejected'.format(pacoteRecebido[0][TCP].dport))
    elif pacoteRecebido[1].haslayer('TCP'):
        print('{} \t {}'.format(pacoteRecebido[1][TCP].sport,pacoteRecebido[1][TCP].sprintf('%flags%')))
            
for pacoteNaoRecebido in uans:
    print('{} \t DROP'.format(pacoteNaoRecebido.dport))