def fib():
	a,b = 0,1
	for i in range(5):
		#print(b)
		yield b  #生成器
		a,b = b,a+b
#print(fib())
G = fib()
print(next(G))
