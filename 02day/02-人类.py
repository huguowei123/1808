class People:
	def eat(self):
		print("吃")
	def drink(self):
		print("喝")
	def sleep(self):
		print("睡")
	def play(self):
		print("玩")
	def introduce(self):
		print("self的年龄是%d self的身高%d"%(self.age,self.height))
man = People()
man.eat()
man.drink()
man.sleep()
man.play()
man.age = 18
man.height = 170
man.introduce()
print(man.age)
print(man.height)


cl = People()
cl.age = 20
cl.height = 180
cl.introduce()
print(cl.age)
print(cl.height)
