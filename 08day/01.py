class Dog():
	def __init__(self):
		self.__age = 100
	def getAge(self):
		return self.__age
	def setAge(self,age):
		self.__age = age
dog = Dog()
dog.setAge(120)
print(dog.getAge())


class Dog():
	def __init(self):
		self.__age = 100
	@property
	def age(self):
		return self.__age
	@
