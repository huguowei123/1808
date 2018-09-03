import pygame
from jingling import *
class PlaneGame(object):  #飞机大战主游戏
	def __init__(self):  #初始化
		#修改游戏中窗口
		self.screen = pygame.display.set_mode(SCREEN_RECT.size)
		#游戏时钟
		self.clock = pygame.time.Clock()
		#调用私有方法，精灵，精灵组创建
		self.__create_sprites()

		pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)   #每秒创建敌机

		pygame.time.set_timer(CREATE_BULLET_EVENT,500)  #每0.5秒创建子弹
		#敌机精灵组
		self.enemy_group = pygame.sprite.Group()
		#子弹精灵组
		self.bullets = pygame.sprite.Group()
		#敌机销毁精灵组
		self.enemy1_down_group = pygame.sprite.Group()
		self.count = 0
		self.score = 0 #分数

	def start_game(self):
		pygame.init()
		while True:
			self.count+=1
			#1.设置刷新帧率
			self.clock.tick(60)
			#2.事件监听
			self.__event_handler()
			#3.碰撞检测
			self.__check_collide()
			#4.更新精灵组
			self.__update_sprites()
			#5.更新屏幕显示
			pygame.display.update()

	def __create_sprites(self):   #创建精灵组和精灵
		bg1 = BackGroundSprite()
		bg2 = BackGroundSprite(True)
		bg2.rect.y = -bg2.rect.height
		self.backgroup = pygame.sprite.Group(bg1,bg2)  #背景组
		self.enemy_group = pygame.sprite.Group()   #敌机组

		#英雄组	
		self.hero = HeroSprite()
		self.hero_group = pygame.sprite.Group(self.hero)

	def __event_handler(self):
		"""事件监听"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				PlaneGame.__game_over()
			elif event.type == CREATE_ENEMY_EVENT:  #定时出现敌机事件
				enemy = EnemySprite() 
				self.enemy_group.add(enemy)
			elif event.type == CREATE_BULLET_EVENT:  #子弹定时器事件
		
				#print("敌机出场")
			
				#enemy = EnemySprite()
				#self.enemy_group.add(enemy)
				self.hero.fire()  #自动发射
		#获取用户按键
		keys_pressed = pygame.key.get_pressed()
		if keys_pressed[pygame.K_RIGHT]:  #移动速度
			self.hero.speed = 10
		elif keys_pressed[pygame.K_LEFT]:
			self.hero.speed = -10
		elif keys_pressed[pygame.K_UP]:
			self.hero.speed1 = -10
		elif keys_pressed[pygame.K_DOWN]:
			self.hero.speed1 = 10
		else:
			self.hero.speed = 0
			self.hero.speed1 = 0

		if keys_pressed[pygame.K_SPACE]:    #手动发射
			#print("发射子弹")
			self.hero.fire()

	def __check_collide(self):
		"""碰撞检测"""
		#敌机精灵组在前并返回敌机精灵
		enemy_down = pygame.sprite.groupcollide(self.enemy_group,self.hero.bullet_group,True,True)   #子弹摧毁敌机
		enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group,True) #敌机撞坏英雄
		enemy1_down_group.add(enemy_down) #加入销毁组
		if len(enemies) > 0:#有内容
			self.hero.kill()
			PlaneGame.__game_over()
		
	def __update_sprites(self):
		"""更新精灵组"""
		self.backgroup.update()
		self.backgroup.draw(self.screen)

		
		self.enemy_group.update()
		self.enemy_group.draw(self.screen)

		self.hero_group.update()
		self.hero_group.draw(self.screen)

		self.hero.bullet_group.update()
		self.hero.bullet_group.draw(self.screen)

		#绘制分数
		self.drawText(str(self.score),SCREEN_RECT.width - 30,50)

		#敌机销毁
		for enemy1_down in enemy1_down_group:
			self.screen.blit(enemy1_down_surface[enemy1_down.down_index],enemy1_down.rect)
			if self.count % 15 == 0:
				enemy1_down.down_index += 1
				if enemy1_down.down_index == 3:
					self.score += 10
					enemy1_down_group.remove(enemy1_down)
					print(self.score)
	@staticmethod
	def __game_over():
		"""游戏结束"""
		print("Game over")
		pygame.quit()
		exit()

	def drawText(self,text,posx,posy,textHeight=48,fontColor=(0,0,0),backgroudColor=(255,255,255)):
		fontObj = pygame.font.Font(None, textHeight)  # 通过字体文件获得字体对象
		textSurfaceObj = fontObj.render(text, True,fontColor,backgroudColor)  # 配置要显示的文字
		textRectObj = textSurfaceObj.get_rect()  # 获得要显示的对象的rect
		textRectObj.center = (posx, posy)  # 设置显示对象的坐标
		self.screen.blit(textSurfaceObj, textRectObj)  # 绘制字

if __name__ == "__main__":
	#创建游戏对象
	game = PlaneGame()
	#开始游戏
	game.start_game()
		
