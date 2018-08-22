def fib():
	a,b = 0,1
	print("--1--")
	for i in range(10):
		print("--2--")
		yield b
		print("--3--")
		a,b = b,a+b
G = fib()
for i in G:
	print(i)

#print(G.__next__())
