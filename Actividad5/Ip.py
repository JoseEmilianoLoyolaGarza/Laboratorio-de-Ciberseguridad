import socket
import urllib.request
import nmap
import base64
import json

hostname = socket.gethostname()

ip_address1 = socket.gethostbyname(hostname)

external_ip = urllib.request.urlopen('https://v4.ident.me').read().decode('utf8')

nl= nmap.PortScanner()

result1=nl.scan(ip_address1)

np= nmap.PortScanner()

result2=np.scan(external_ip)

text1=json.dumps(result1)
text2=json.dumps(result2)

iplocal=ip_address1.encode("utf-8")
ippublica=external_ip.encode("utf-8")
scan1=text1.encode("utf-8")
scan2=text2.encode("utf-8")

code = open('C:/Users/logaa/Pictures/Facultad/TercerSemestre/Laboratorio/Actividad5/Ips.txt', 'wb') 
code.write(base64.b16encode(iplocal))
code.write(base64.b16encode(ippublica))
code.write(base64.b16encode(scan1))
code.write(base64.b16encode(scan2))
code.close()