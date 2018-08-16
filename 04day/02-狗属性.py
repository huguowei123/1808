class Dog():
	def dog(self):
		self.name = "艾琳"
		self.age = "10"
	def set(self,name,age):
		self.__name = name
		self.__age = age  
	def get(self):
		return(self.__name,self.__age)
dog = Dog()
dog.set("艾琳",10)
print(dog.get())
