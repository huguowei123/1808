from socket import *
s = socket(AF_INET,SOCK_STREAM)#创建tcp
s.bind(("",1234)) #绑定

s.listen(5)  #监听

s1.info = s.accept()  #等着接电话
print("有新链接")

print(s1.recv(1024).decode("gb2312")) #接收
s1.send("哈哈".encode("gb2312"))

s1.close()
s.close()
