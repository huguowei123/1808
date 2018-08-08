class Car():
	def __init__(self,color,type):
		self.color = color
		self.type = type
	def __str__(self):
		msg ="颜色%s,型号%s"%(self.color,self.type)
		return msg
	def move(self):
		print("跑")
	def listen(self):
		print("听音乐")
dazhong = Car("red","dazhong1")
dazhong.move()
dazhong.listen()
#dazhong.introduce()
print(dazhong)

benchi = Car("blue","benchi350")
print(benchi)
