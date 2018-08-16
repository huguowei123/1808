class Game():
	count = 3
	def __init__(self,name):
		self.name = name

	def play(self):  #实例方法
		print("一起玩")

	@classmethod
	def getCount(cls):
		return cls.count

	@staticmethod
	def print_menu():
		print("1.开始游戏")
		print('2.结束')

cq = Game("王者")

print(cq.name)  #调实例属性
cq.play()    #调实例方法

print(Gane.count)   #调类属性
Game.getCount()   #通过类调用类方法
cq.getCount()   #通过实例调用类方法

Game.print_menu()   #通过类调静态方法
cq.print_menu()   #通过实例调用静态方法
