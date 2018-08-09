class QQ():
	def openvip(self):
		print("开会员成功")
	def checkqq(self,money):
		if money > 10:
			self.openvip()
		else:
			print("开不了")
qq = QQ()
qq.checkqq(12)

qq1 = QQ()
qq1.checkqq(8)
