#coding=utf-8
class Dog():
	def __init__(self):
		self.name = "大黄"
		print("init")
	def __str__(self):
		return "str方法"
	def __del__(self):
		print("我del")
dog = Dog()
print(dog)
dog1 = dog
print(id(dog))
print(id(dog))
del dog
del dog1
print("haha")
