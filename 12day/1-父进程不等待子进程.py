import os 
import time
pid = os.fork()
if pid == 0:
	time.sleep(3)
	print("子进程")
else:
	print("父进程")
