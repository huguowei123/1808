class Beifen():
	def beifen(self):
		name = input("输入备份文件名")
		f = open(name,"r")
		content = f.rfind(".")
		newname = name[:positin]+"备份"+name[:position]
		f1 = open(name,"w")
		while True:
			content = f1.read(1024)
			f1.write = content
			if len(content) == 0:
				break
			f.close()
			f1.close()
a = Beifen()
a.beifen()
