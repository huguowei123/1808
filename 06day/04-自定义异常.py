class ShowError(Exception):
	def __init__(self,name):
		self.name = name
class Input():
	def input(self):
		self.name = input("输入名字")
		try:
			if self.name == "老王":
				raise ShowError(self.name)
		except ShowError as ret:
			print("输入%s报错"%ret.name)
i = Input()
i.input()
	
