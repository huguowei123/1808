class Dog():
	def eat(self):
		print("吃狗粮")
	def wark(self):
		print("汪汪")
	def __init__(self,name,age):
		self.name = name
		self.age = age
hashiqi = Dog("二哈",10)
hashiqi.wark()
hashiqi.eat()
print(hashiqi.name)
print(hashiqi.age)
