import os
import webbrowser
import time

print("Subscribe")
time.sleep(1.2)
webbrowser.open("https://t.me/termuxqew")
print("\033[31m                                            ")
print("\033[31m                      -//.                  ")
print("\033[31m                    `yddddo`                ")
print("\033[31m           -oho.   .sddddddo`   -oh+.       ")
print("\033[31m        ./ys:`/ys:odddddddddd+/yy:`/yy/`    ")
print("\033[31m      `sy/`     /ddddohsohsdddd-     .+ys`  ")
print("\033[31m           .:`  yddds++++++ydddo  `:.       ")
print("\033[31m         .ohoho/dd+s-ooooo+++odd:ohoho.     ")
print("\033[31m       .oh/` `:yddsh-ooooo++yydds:  `+ho.   ")
print("\033[31m    .`      +ssssddddhdhhdhddddssss+      `.")
print("\033[31m           +d-    .sddddddddo.  ``-d/       ")
print("\033[31m          /d-       `-///:-        :d:      ")
print("\033[31m         :d:                        /d-     ")
print("\033[31m        -d/                          +d.    ")
print("\033[31m        .:                            :-    ")
print("""+------------------------------+
	 |github.com/fuckwbored/spydra	|
	 |t.me/termuxqew             	|
	 +------------------------------+
""")
print("\033[48;5;236m\033[38;5;231 Spydra \033[38;5;208mToolKit\033[0;0m")
print("---------------                 --------------------------")
print("TERMUX & LINUX TOOLS")
print("[+] lfi_scanner			lfi vulnerability detecter")
print("[+] dir_scanner			admin panel finder")
print("[+] port_scanner                tcp port scanner")
print("[+] upload_panel_scanner        simple upload panel finder")
print("[+] submit_forms_finder         website's submit forms scrapper")
print("LINUX TOOLS")
print("[+] packet_sniffer              simple http packet sniffer")
print("")
print("")
try:
  while True:
    menu = input(">")
    if menu == "lfi_scanner":       
        print("\033[1;31;40m Script to detect LFI vulnerability \033[0m")
        os.system("cd LFI && python3 tool1.py")
    elif menu == "dir_scanner":
	     print("Script to find admin panels")
	     os.system("cd DIR && python3 tool2.py")
    elif menu == "upload_panel_scanner":
      os.system("cd UPLOAD && python3 upload.py")
    elif menu == "port_scanner":
      os.system("cd PORT && python3 port_scanner.py")
    elif menu == "packet_sniffer":
      os.system("cd SNIFF && python3 sniffer.py")
    elif menu == "submit_forms_finder":
      os.system("cd FORM && python3 form.py")
    else:
       print("Use name of tool")

except KeyboardInterrupt: 
        print("\n Bye!") 
