from scapy.all import *

interface = "eth0"
ip_range = "10.10.0.0/24"
broadcast_mac = "ff:ff:ff:ff:ff:ff"

packet = Ether(dst=broadcast_mac)/ARP(pdst = ip_range)

ans, unans = srp(packet, timeout = 2, iface=interface, inter=0.1)

for send, receive in ans:
    print(receive.sprintf(r"%Ether.src% - %ARP.psrc%"))
