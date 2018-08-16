class Beifen():
	def beifen(self):
		name = input("输入备份文件名")
		f = open(name,"r")
		position = f.rfind(".")
		newname = name[:position]+"备份"+name[position:]
		f1 = open(newname,"w")
		while True:
			content = f.read(1024) 
			f1.write(content)
			if len(contene)	== 0:
				break
		f.close()
		f1.close()
a = Beifen()
a.beifen()
