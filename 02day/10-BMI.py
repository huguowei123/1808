class person():
	def tizhi(self):
		a = float(input("输入身高"))
		b = float(input("输入体重"))
		x = b/a**2
		if x < 18.5:
			print("过轻")
		elif x >= 18.5 and x < 25:
			print("正常")
		elif x >= 25 and x < 28:
			print("过重")
		elif x >=28 and x <32:
			print("肥胖")
		elif x >= 32:
			print("严重肥胖")
c = person()
c.tizhi()
