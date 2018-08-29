import re 
def my_name():
	ret = re.match(r"<(?P<name>)\w*><(?P<name1>)\w>.*</(?P=name1)>/<?(P=name)>",s)
	if ret:
		print("a")
	else:
		print("b")	
