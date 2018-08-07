class mingpian1():
	def mingpian(self):
		while True:
			print("1:添加")
			print("2:查看")
			print("3:退出")
			a = input("选择功能")
			if a == "1":
				list = []
				f = open("名片.txt","b")
				name = input("输入名字")
				age = input("输入年龄")
				list.append(name)
				list.append(age)
				f.write(str(list)+"\n")
				f.close()
				print("成功")
			elif a == "2":
				f = open("名片.txt","r")
				b = f.read()
				print(b)
				f.close()
			elif a == "3":
				break
c = mingpian1()
c.mingpian()
