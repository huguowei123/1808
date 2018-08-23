from multiprocessing import Pool
import time
def download():
	for i in range(10):
		#print("下载%d%%"%(i*10))
		time.sleep(1)
	return "下载完成"
def noti(arg):
	print(arg)
p = Pool()

p.apply_async(download,callback=noti)
p.close()
for i in range(50):
	print("看电影中")
	time.sleep(1)
