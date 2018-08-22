class SS():
	def sushu(self):
		for i in range(2,101):
			flag = 0
			for a in range(2,i):
				if i%a == 0:
					flag = 1
					i += 1
					break
			if flag == 0:
				print(i)
a = SS()
a.sushu()
