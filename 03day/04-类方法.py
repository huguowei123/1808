class Dog():
	print("哈哈")
	count = 10   #类属性
	__count1 = 20 #私有属性
	
	def __init__(self,name):
		self.name = name   #实例属性
		self.__age = 10   #私有属性
	
	def getAge(self):
		return self.__age

	def getCount1(self):
		return Dog.count

	@classmethod
	def getCount(cls):
		print("类方法")
		return cls.count

	@classmethod
	def getCount(cls):
		return cls.__count1


tom = Dog("Tom")  #创建实例对象
print(tom.name)
print(tom.ageAge())


#print(Dog.count)  #通过类访问类属性

Dog.getCouont()   #通过类访问类方法
#tom.getCount()   #通过对象访问类方法


#print(tom.getCoount1())


#print(Dog.__count1)   #不能访问私有类属性
print(Dog.getCount1())  #通过公有方法访问私有类属性
