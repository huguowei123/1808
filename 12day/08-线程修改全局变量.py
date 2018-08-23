from threading import Thread
import time
num = 0
flag = 1
def work1():
	global num,flag
	if flag == 1:
		for i in range(1000):
			num+=1
		print("Thread-1")
		print(num)	
def work2():
	global num
	while True:
		if flag == 2:
			for i in range(1000):
				num+=1
			print("Thread-2")
			print(num)
			break
t1 = Thread(target=work1,args=())
t1.start()
#t1.join()  #t1完了t2开始
t2 = Thread(target=work1,args=())
t2.start()


