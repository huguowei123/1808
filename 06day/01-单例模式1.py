class Son():
	__instance = None
	__flag = False
	def __init__(self,name):
		if Son.__flag == False:
			self.name = name
			self.__flag = True

	def __now__(cls,*args,**kwargs):
		if cls.__instance == None:
			cls.__instance = super().__new__(cls)
			return cls.__instance
		else:
			return cls.__instance
xifu = Son("小红")
print(id(xifu))
xifu1 = Son("小绿")
print(id(xifu1))
	
