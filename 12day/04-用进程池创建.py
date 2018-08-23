from multiprocessing import Pool
import time
def show():
	for i in range(10):
		time.sleep(1)
		print("hehe")
p = Pool()  #创建一个池子，可以装无数个
for i in range(3):
	#p.apply_async(show) #添加一个进程到池子李非阻塞添加进程，3进程同时进行
	p.apply(show)  #阻塞添加进程，3个程序依次进行
	print("ok")
p.close()  #关池子
p.join() #不支持传超时时间
print("haha")
