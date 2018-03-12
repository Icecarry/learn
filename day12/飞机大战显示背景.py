"""
飞机大战，加载背景
"""
import pygame
import time


# 创建窗口
screen = pygame.display.set_mode((480, 852), 0, 32)

# 加载图片
bg = pygame.image.load('feiji/background.png')

# 加载玩家飞机
hero = pygame.image.load('feiji/hero1.png')

# 绑定图片到窗口
screen.blit(bg, (0, 0))

# 绑定玩家飞机到窗口
screen.blit(hero, (190, 728))

# 刷新图片
pygame.display.update()

time.sleep(60)
