import os
pid = os.fork()
print(pid)
if pid == 0:
	print("子进程pid=%d 父进程的pid=%d"%(os.getpid(),os.getppid()))

else:
	print("父进程pid=%d 父父pid=%d"%(os.getpid(),os.getppid()))
