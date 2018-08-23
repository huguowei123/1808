'''
class Dog():
	def __init__(self):
		self.__age = 10
	def getAge(self):
		return self.__age
	def setAge(self,age):
		self.__age = age

	age = property(getAge,setAge)
dog = Dog()
#dog.setAge(12)
#print(dog.getAge())
dog.age = 12
print(dog.age)
'''
class Dog():
	def __init__(self):
		self.__age = 10
	def getAge(self):
		return self.__age
	def setAge(self,age):
		self.__age = age
	age = property(getAge,setAge)
dog = Dog()
dog.age = 12
print(dog.age)





age = property(getAge,setAge)
















