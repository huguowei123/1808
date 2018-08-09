import time
import random
class Person():
	def __init__(self,name):
		self.name = name
		self.gun = None   #初始没枪
		self.hp = 100   #血量
	def zhuangzidan(self,zidan,danjia):  #装子弹
		danjia.addzidan(zidan)

	def zhuangdanjia(self,danjia,gun):    #装弹夹
		gun.addDanjia(danjia)

	def nagun(self,gun):    #拿枪
		self.gun = gun

	def kaihuo(self,diren):    #开火
		self.gun.kaihuo(diren)

	def diaoxue(self,count):   #子弹伤害量
		self.hp -= count
		if self.hp <= 0:
			print("挂了血量剩%d"%self.hp)
			break
		else:
			print("敌人%s还剩%d"%(self.name,self.hp))
class Gun():
	def __init__(self,name):
		self.name = name
		self.danjia = None
	
	def addDanjia(self,danjia):
		self.danjia = danjia

	def kaihuo(self,diren):
		zidan = self.danjia.tanzidan()   #弹出一个子弹
		zidan.sharen(diren)

class Danjia():
	def __init__(self,count):   #弹容量
		self.count = count
		self.zidans = []    #子弹列表

	def addzidan(self,zidan):    #装子弹
		self.zidans.append(zidan)
	def tanzidan(self):      #弹子弹
		return self.zidans.pop(0)

class Zidan():
	def __init__(self,name,hurt):
		self.name = name
		self.hurt = hurt

	def sharen(self,diren):
		diren.diaoxue(self.hurt)

laowang = Person("老王")
print("老王出现了")
time.sleep(1)
ak47 = Gun("ak47")
print("出现一吧ak")
time.sleep(1)
danjia = Danjia(40)
print("装弹中")
for i in range(40):
	zidan = Zidan("7.62",random.randint(1,100))
	laowang.zhuangzidan(zidan,danjia)
laowang.zhuangdanjia(danjia,ak47)
time.sleep(3)
laowang.nagun(ak47)
laosong = Person("老宋")   #敌人
for i in range(30):
	time.sleep(1)
	print("老王开枪")
	laowang.kaihuo(laosong)
