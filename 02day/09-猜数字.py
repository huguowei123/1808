class shu():
	def suan(self):
		import random
		a = random.randint(1,100)
		for i in range(1,11):
			b = int(input("猜的数字"))
			if b > a:
				print("大了")
			elif b < a:
				print("小了")
			elif b == a:
				print("对啦")	
				break
a = shu()
a.suan()
