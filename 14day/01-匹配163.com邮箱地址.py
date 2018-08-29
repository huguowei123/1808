import re
def checkyouxiang(youxiang):
	ret = re.match(r"\w{4,20}@(163|qq|139)\.com",youxiang)
	if ret:
		print("合法")
	else:
		print("非法")
ret = checkyouxiang("esfefs@qq.com") 
ret = checkyouxiang("12347654@163.com") 
