import socket

s = scoket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in [b'Arlex',b'Happy',b'Altynai']:
	s.sendto(data,(127.0.0.1),9999)
	print(s.recv(1024).decode('utf-8'))
s.close()