import os
b = input("输入批量重命名文件夹名字")
files = os.listdir(b)
os.chdir(b)
print(os.getcwd())
for i in files:
	position = i.rfind(".")
	newname = i[:position]+"-腾讯"+i[position:]
	os.rename(i,newname)
