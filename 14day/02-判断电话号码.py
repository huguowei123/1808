import re
def checkphone(phone):
	ret = re.match("^1[3456789]\d{9}$",phone)
	if ret:
		print("合法")
	else:
		print("非法")
ret = checkphone("13245678934")
ret = checkphone("1393432468")
