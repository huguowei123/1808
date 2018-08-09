import random
class Digua():
	def __init__(self):
		self.status = "生得"
		self.times = 0
		self.zl = []
	def __str__(self):
		msg = "烤的程度是%s"%self.status
		return msg+str(self.zl)
	def cook(self,time):
		self.times+=time
		if self.times >= 1 and self.times <= 3:
			self.status = "生得"
		elif self.times >= 3 and self.times <= 5:
			self.status = "半生"
		elif self.times >= 6 and self.times <= 9:
			self. status = "八分"
		elif self.times >= 10 and self.times <= 12:
			self.status = "熟了"
		elif self.times  > 12:
			self.status = "糊了"
	def addzl(self,name):
		self.zl.append(name)
list = ["米","面","油","醋","糖"]
digua = Digua()
for i in range(5):
	digua.cook(random.randint(1,4))
	zl = random.choice(list)
	list.remove(zl)
	digua.addzl(zl)
	print(digua)
