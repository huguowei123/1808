class Car():
	def __init__(self,color,type):
		self.color = color
		self.type = type
	def move(self):
		print("跑")
	def listen(self):
		print("听")
	def __str__(self):
		msg = print("颜色%s,型号%s"%(self.color,self.type))
		return msg
dazhong = Car("red","dazhong1")
dazhong.move()
dazhong.listen()
#dazhong.introduce()
