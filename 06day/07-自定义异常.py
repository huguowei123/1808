class showError(Exception):
	def __init__(self,len):
		self.len = len
		self.leastLen = 5
name = input("输入名字")
try:
	if len(name) < 5:
		raise showError(len(name))
except showErrror as ret:
	print("至少需要%d位，传的值是%d"%(ret.leastLen,ret.len))

