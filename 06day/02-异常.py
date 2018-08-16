try:
	open("1.txt","r")
	#print(name)
	11/0
	print("老王")
	print(1+1)
except(FileNotFoundError,NameError):
	print("错")
except Expection as ret:
	print("报错",ret)
else:
	print("没错")
finally:
	print("不管错不错")
