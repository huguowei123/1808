class Sushu():
	def sushu(self):
		for i in range(2,101):
			flag = 1
			for a in range(2,i):
				if i%a == 0:
					flag = 0
					break
			if flag == 1:
				print(i)
ss = Sushu()
ss.sushu()
