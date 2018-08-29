from socket import *
s = socket(AF_INET,SOCK_STREAM)
s.connect(("192.168.43.85",8080))

s.send("hehe".encode("gb2312"))
while True:
	msg = s.recv(1024).decode("gb2312")
	print(msg)
