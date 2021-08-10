import requests

text_file = open("wordlist.txt", "r")
url = input("[?] Enter target url: ")

for line in text_file.readlines():
        targt = url + '/' + line
        r = requests.get(targt.format(line))

        if r.status_code == 200:
        	  payload = ("[+] Path -> {}".format(line))
        	  print(payload)