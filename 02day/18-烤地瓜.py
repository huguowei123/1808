import random
class Digua():
	def __init__(self):
		self.status = "shengde"
		self.times = 0
		self.zl = []
	def __str__(self):
		msg = "烤的程度是%s"%self.status
		return msg+str(self.zl)
	def cook(self,time):
		self.times+=time
		if self.times >= 1 and self.times <= 2:
			self.status = "shengde"
		elif self.times >= 3 and self.times <= 5:
			self.status = "bansheng"
		elif self.times >= 6 and self.times <= 9:
			self.status = "bafen"
		elif self.times >= 10 and self.times <= 12:
			self.status = "shu"
		elif self.times > 12:
			self.status = "hu"
	def addzl(self,name):
		self.zl.append(name)
list = ['菜','米','面','油','糖']
digua = Digua()
for i in range(5):
	digua.cook(random.randint(1,4))
	zl = random.choice(list)
	list.remove(zl)
	digua.addzl(zl)
	print(digua)
		
