import random
import pygame
SCREEN_RECT = pygame.Rect(0,0,480,700)
CREATE_ENEMY_EVENT = pygame.USEREVENT 
class GameSprite(pygame.sprite.Sprite):  #父类
	def __init__(self,imagename,speed=1,speed1=1):
		super().__init__()   #调用父类方法
		self.image = pygame.image.load(imagename)
		self.rect = self.image.get_rect()
		self.speed = speed
		self.speed1 = speed1
	def update(self):
		self.rect.y+=self.speed
  
class EnemySprite(GameSprite):   #敌机子类
	def __init__(self):
		self.imagename = "/home/huiguowei/桌面/1808/07day/images/enemy0.png"
		super().__init__(self.imagename)
		self.speed = random.randint(1,3)
		self.rect.bottom = 0
		max_x = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0,max_x)

	def update(self):
		super().update()
		if self.rect.y >= SCREEN_RECT.height:
			self.kill()
			#print("销毁")

class BackGroundSprite(GameSprite):
	def __init__(self,is_alt=False):
		self.imagename = "/home/huiguowei/桌面/1808/07day/images/background.png"
		super().__init__(self.imagename,10)
		if is_alt:
			self.rect.y = - self.rect.height

	def update(self):
		super().update()
		if self.rect.top >= SCREEN_RECT.height:
			self.rect.y = -self.rect.height
class HeroSprite(GameSprite):  
	#英雄精灵
	def __init__(self):
		self.imagename = "/home/huiguowei/桌面/1808/07day/images/hero.gif"
		super().__init__(self.imagename,0)
		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = 650
		self.bullet_group = pygame.sprite.Group()
	def update(self):
		#self.update()
		self.rect.x+=self.speed

		if self.rect.left <= 0:
			self.rect.left = 0

		if self.rect.right >= SCREEN_RECT.width:
			self.rect.right = SCREEN_RECT.width

		self.rect.y+=self.speed1
		if self.rect.top <= 0:
			self.rect.top = 0

		if self.rect.bottom >= SCREEN_RECT.height:
			self.rect.bottom = SCREEN_RECT.height

	def fire(self):
		bullet = BulletSprite()
		bullet.rect.centerx = self.rect.centerx
		bullet.rect.y = self.rect.top - 10
		self.bullet_group.add(bullet)

		
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
		if self.rect.bottom <= 0:
			self.kill()
