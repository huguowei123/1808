class Dog():
	def __init__(self):
		self.__name = "艾琳"
		self.__age = 12
	def run(self):
		print("跑")
	def set(self,name,age):
		self.__name = name
		self.__age = age
	def get(self):
		return(self.__name,self.__age)
dog = Dog()
dog.set("艾琳",12)
dog.run()
print(dog.get())
