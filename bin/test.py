import requests

SERVER_IP = ''
SERVER_PORT = '8000'

OBFUSCATE_URL = 'http://{ip}:{port}/obfuscate'.format(ip=SERVER_IP,port=SERVER_PORT)
DEOBFUSCATE_URL = 'http://{ip}:{port}/deobfuscate'.format(ip=SERVER_IP,port=SERVER_PORT)

response = requests.post(OBFUSCATE_URL,data='http://askcorona.com//img1.wsimg.com/blobby/go/ce07de95-d1c8-4cea-9d63-59054f23b2e4/downloads/covid-19-daily-data-summary%201329pm.pdf?ver=1585511192789').json()
print(response)


response = requests.post(DEOBFUSCATE_URL,data='hxxp://askcorona[.]com//img1.wsimg.com/blobby/go/ce07de95-d1c8-4cea-9d63-59054f23b2e4/downloads/covid-19-daily-data-summary%201329pm.pdf?ver=1585511192789').json()
print(response)