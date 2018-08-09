import random
class Home():
	def __init__(self,area,type,address):
		self.area = area
		self.type = type
		self.address = address
		self.jiaju = []
	def __str__(self):
		msg = "面积是%d,户型%s,地址是%s,家具有%d个"%(self.area,self.type,self.address,len(self.jiaju))
		return msg
	def add(self,jj):
		self.jiaju.append(jj)
	def tell_area(self):
		all_a = 0
		for i in self.jiaju:
			all_a+=i.area
		diff = self.area - all_a
		return diff
class Bed():
	def __init__(self,area,name):
		self.area = area
		self.name = name
home = Home(540,"四合院","长安街")
for i in range(100):
	bed = Bed(random.randint(8,12),"单人床")
	if home.tell_area() < bed.area:
		break
	home.add(bed)
print(home)
