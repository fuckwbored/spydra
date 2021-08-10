import socket 
from datetime import datetime 
import os

print('simple TCP port sacnner')     

url = input("[?] Enter domain (ex: scanme.nmap.org)> ")
target = socket.gethostbyname(url)  

print("-" * 50)  
print("Scanning started at:" + str(datetime.now())) 
print("-" * 50) 

try:
    for port in range(1,65535): 

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        socket.setdefaulttimeout(1) 

        result = s.connect_ex((target,port)) 
        if result ==0:
        	print("033[1;34;40m [+] Port {} open \033[0m".format(port))
        	os.system("whatportis {}".format(port)) 
        s.close() 

except socket.gaierror: 
        print("\n Hostname Could Not Be Resolved !!!!")  
except socket.error: 
        print("\ Server not responding !!!!") 
except KeyboardInterrupt: 
        print("\n Bye!") 