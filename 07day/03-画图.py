import pygame
import sys
from pygame.locals import *


# pygame 初始化
pygame.init()


# 设置背景颜色和线条颜色
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


# 设置鼠标拖动标志位
POS_moving = False


# 设置背景框大小
size = width, height = 600, 600
position = width // 2, height // 2


# 设置帧率，返回clock 类
clock = pygame.time.Clock()


screen = pygame.display.set_mode(size)
pygame.display.set_caption("llls make")


while True:
	for event in pygame.event.get():
# 查找关闭窗口事件
		if event.type == QUIT:
			sys.exit()


	# 查找鼠标按下事件
		elif event.type == MOUSEBUTTONDOWN:
			if event.button == 1:
				# 值标志位为正
				POS_moving = True


	# 查找鼠标松开事件
		elif event.type == MOUSEBUTTONUP:
			if event.button == 1:
			# 置标志位为假
				POS_moving = False

# 填充背景色
screen.fill(WHITE)


# 画三个同心圆
pygame.draw.circle(screen, GREEN, position, 25, 1)
pygame.draw.circle(screen, BLUE, position, 75, 1)
pygame.draw.circle(screen, RED, position, 125, 1)

# 拖拽圆
if POS_moving:
	position = pygame.mouse.get_pos()


# 刷新图
pygame.display.flip()


clock.tick(60)
