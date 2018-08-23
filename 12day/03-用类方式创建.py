from multiprocessing import Process
import time
class MyProcess(Process):
	def __init__(self):
		super(). __init__()
	def run(self):
		for i in range(10):
			time.sleep(1)
			print("我爱你")
p = MyProcess()
#p1 = MyProcess()
p.start()
#p1.start()
p.join(3)
print("吃喝")
