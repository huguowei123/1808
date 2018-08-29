from socket import *
udpSocket = socket(AF_INET,SOCK_DGRAM)
udpSocket.sendto("哈哈哈".encode("gb2312"),("192.168.56.1",8080))
udpSocket.close()
