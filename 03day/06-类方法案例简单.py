class DateTool():
	def __init__(self,y,m,d):
		self.y = y
		self.m = m 
		self.d = d 

	def print_show(self):
		print("今天%s年%s月%s日"%(self.y,self.m,self.d))

	@classmethod
	def del_Date(cls,date):
		y,m,d = str.split("-")
		return y,m,d

str = "2018-08-10"
y,m,d = str.split("-")
dt = DateTool(y,m,d)
dt.print_show()

str = "2018-08-10"
DateTool.del_date(str)
