class beifen:
	def bf(self):
		name = input("输入备份文件名")
		f = open(name,"r")
		content = f.read()
		position = name.rfind(".")
		newname = name[:position]+"备份"+name[position:]
		f1 = open(newname,"w")
		while True:
			content = f.read(1024)
			f1.write(content)
			if len(content) == 0:
				break
			f.close()
			f1.close()
u = beifen()
u.bf() 
