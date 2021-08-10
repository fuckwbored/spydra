import requests

text_file = open("Payloads.txt", "r")
url = input("[?] Enter target url:")

robotstxt = url + '/' + 'robots.txt'
robots = requests.get(robotstxt)
robots1 = requests.get(robotstxt).text

if robots.status_code == 200:
	print("\033[0;37;41mrobots.txt file detected!\033[0m")
	print(robots1)


for line in text_file.readlines():
        targt = url + '/' + line
        r = requests.get(targt.format(line))

        if r.status_code == 200:
        	  payload = ("Path -> {}".format(line))
        	  print(payload)