import pygame
from jingling import *
pygame.init()
screen = pygame.display.set_mode((480,700))
bg = pygame.image.load("/home/huiguowei/桌面/1808/07day/images/background.png")
#bg = pygame.image.load("./images/game_loading1.png")
#screen.blit(tx,(0,0))  #原点颜色覆盖
#pygame.display.update()
hero = pygame.image.load("/home/huiguowei/桌面/1808/07day/images/hero1.png")
#screen.blit(hero,(200,500))
  
hero_rect = pygame.Rect(200,500,150,150)
#screeen.blit(hero,herorect)
  
clock = pygame.time.Clock()   #创建时钟
  
enemy = EnemySprite()  #创建敌机精灵
enemy1 = EnemySprite() #创建敌机精灵
enemy2 = EnemySprite()
enemy1.rect.x = 50
enemy1.rect.y = 100
enemy1.speed = 2
enemy_group = pygame.sprite.Group(enemy,enemy1,enemy2)
  
while True:
	clock.tick(60)   #一秒60
	hero_rect.y -= 1   #速度
	screen.blit(bg,(0,0))
	screen.blit(hero,hero_rect)
	if hero_rect.bottom <= 0:    #返航
		hero_rect.top = 700
	enemy_group.update()    #更新
	enemy_group.draw(screen)   #画到哪
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print("退出")
			pygame.quit()
			exit()

