class Dog():
	def __init__(self):
		self.name =""
		self.__age = 0
	def sleep(self):
		print("sleep")
	def setAge(self,age):
		self.age = age
		if age < 1 or age > 15:
			print("不符合")
		else:
			self.__age = age
	def getAge(self):    #公有方法
		return self.__age
dog = Dog()
dog.setAge(10)
print(dog.getAge())
