import random
import pygame
SCREEN_RECT = pygame.Rect(0,0,480,700) #屏幕大小
CREATE_ENEMY_EVENT = pygame.USEREVENT   #敌机定时器事件常量
CREATE_BULLET_EVENT = pygame.USEREVENT + 1   #子弹时间常量
#爆炸销毁图片
bg1 = pygame.image.load("/home/huiguowei/桌面/1808/07day/images/enemy0_down1.png")
bg2 = pygame.image.load("/home/huiguowei/桌面/1808/07day/images/enemy0_down2.png")
bg3 = pygame.image.load("/home/huiguowei/桌面/1808/07day/images/enemy0_down3.png")

bg4 = pygame.image.load("/home/huiguowei/桌面/1808/07day/images/enemy0_down4.png")
#爆炸精灵组
enemy1_down_group = pygame.sprite.Group()
#爆炸图片放到列表中
enemy1_down_surface = []
enemy1_down_surface.append(bg1)
enemy1_down_surface.append(bg2)
enemy1_down_surface.append(bg3)
enemy1_down_surface.append(bg4)

class GameSprite(pygame.sprite.Sprite):  #父类
	def __init__(self,imagename,speed=1,speed1=1):
		super().__init__()   #调用父类方法
		self.image = pygame.image.load(imagename)
		self.rect = self.image.get_rect()
		self.speed = speed
		self.speed1 = speed1
	def update(self):
		self.rect.y+=self.speed

  
class EnemySprite(GameSprite):   #敌机精灵
	def __init__(self):
		self.imagename = "/home/huiguowei/桌面/1808/07day/images/enemy0.png"
		super().__init__(self.imagename)
		self.speed = random.randint(1,3)  #敌机随机出现速度
		self.rect.bottom = 0  #随机初始位置
		max_x = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0,max_x)

		#self.rect.bottom = 0

		self.down_index = 0  #敌机销毁图片索引

	def update(self):
		super().update()
		if self.rect.y >= SCREEN_RECT.height:   #敌机飞出屏幕
			self.kill()
			#print("销毁")
	def __del__(self):
		pass
		#print("敌机挂了%s"self.rect)
class BackGroundSprite(GameSprite):  #背景精灵
	def __init__(self,is_alt=False):
		self.imagename = "/home/huiguowei/桌面/1808/07day/images/background.png"
		super().__init__(self.imagename,10)
		#if is_alt:
			#self.rect.y = - self.rect.height

	def update(self):
		super().update()
		#若移出屏幕，将图像设置到屏幕上方
		if self.rect.top >= SCREEN_RECT.height:
			self.rect.y = -self.rect.height
class HeroSprite(GameSprite):  
	#英雄精灵
	def __init__(self):
		self.imagename = "/home/huiguowei/桌面/1808/07day/images/hero.gif"
		super().__init__(self.imagename,0)
		self.rect.centerx = SCREEN_RECT.centerx  #初始位置
		self.rect.bottom = 650
		self.bullet_group = pygame.sprite.Group()
	def update(self):
		#self.update()
		self.rect.x+=self.speed  #水平移动

		if self.rect.left <= 0:   #边界横向
			self.rect.left = 0

		if self.rect.right >= SCREEN_RECT.width:
			self.rect.right = SCREEN_RECT.width

		self.rect.y+=self.speed1  #纵向
		if self.rect.top <= 0:
			self.rect.top = 0

		if self.rect.bottom >= SCREEN_RECT.height:
			self.rect.bottom = SCREEN_RECT.height

	def fire(self):
		bullet = BulletSprite()  #创子弹精灵
		bullet.rect.centerx = self.rect.centerx #精灵位置
		bullet.rect.y = self.rect.top - 10
		self.bullet_group.add(bullet) #精灵添到精灵组

		
		bullet1 = BulletSprite()
		bullet1.rect.centerx = self.rect.centerx - 35
		bullet1.rect.y = self.rect.top + 35
		self.bullet_group.add(bullet1)

		
		bullet2 = BulletSprite()
		bullet2.rect.centerx = self.rect.centerx + 35
		bullet2.rect.y = self.rect.top + 35
		self.bullet_group.add(bullet2)

class BulletSprite(GameSprite):   #子弹精灵
	def __init__(self):
		self.imagename = "/home/huiguowei/桌面/1808/07day/images/bullet.png"
		super().__init__(self.imagename,-20)

	#def __del__(self):
		#print("子弹销毁")
	def update(self):
		super().update()
		if self.rect.bottom <= 0:  #超出屏幕删除
			self.kill()
