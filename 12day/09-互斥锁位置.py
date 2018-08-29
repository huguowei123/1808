from threading import Thread,Lock
import time
num = 0
def work1():
	global num
	for i in range(100000):
		m.acquire(True)   #加锁 阻塞加锁
		num+=1
		m.release() #释放锁
	print(num)	
	print("Thread-1")
def work2():
	global num
	for i in range(100000):
		m.acquire(True)
		num+=1
		m.release()
	print(num)
	print("Thread-2")
m = Lock()
t1 = Thread(target=work1,args=())
t1.start()
#t1.join()  #t1完了t2开始
t2 = Thread(target=work1,args=())
t2.start()


