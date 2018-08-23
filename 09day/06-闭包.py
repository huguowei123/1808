def show(num):
	def inner(a,b):
		return a+b+num
	return inner
a = show(1)
print(a(1,2))
