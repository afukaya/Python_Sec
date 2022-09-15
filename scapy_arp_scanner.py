from scapy.all import *

def display_arp_pkt(pkt):
    if pkt[ARP].op == 1:
        return f'request: {pkt[ARP].psrc} requests {pkt[ARP].pdst}'
    if pkt[ARP].op == 2:
        return f'response: {pkt[ARP].psrc} MAC is {pkt[ARP].hwsrc}'

sniff(prn=display_arp_pkt, filter='arp', store=0)