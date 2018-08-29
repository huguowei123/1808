class Car():
	def __init__(self,color):
		self.color = color
	def run():
		print("跑")
class BWM(Car):
	def run():
		print("宝马跑")
class BENCHI(Car):
	def run():
		print("奔驰跑")
class AODI(Car):
	def __init__(self,color):
		self.color = 6
		super().__init__(color)
	def run(self):
		print("奥迪跑")
class Factory():
	def create(self):
		pass
class CarFactory(self,Name):
	self.Name = Name
	if self.Name == 1:
		self.car = "BWM"
	elif self.Name == 2:
		self.car = "BENCHI"
	else:
		self.car = "AODI"
		

bwm = BWMFactory().create()
benchi = BENCHIFactory.create()
aodi = AODIFactory().create()
		
