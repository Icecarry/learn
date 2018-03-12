"""
飞机大战，加载背景
"""
import pygame
import time
from pygame.locals import *


class HeroPlane(object):

    def __init__(self):
        self.x = 190
        self.y = 728

        imagepath = 'feiji/hero1.png'
        self.image = pygame.image.load(imagepath)


def main():
    # 创建窗口
    screen = pygame.display.set_mode((480, 852), 0, 32)

    # 加载图片
    bg = pygame.image.load('feiji/background.png')

    # 加载玩家飞机
    hero = HeroPlane()
    # hero = pygame.image.load('feiji/hero1.png')
    # x = 190
    # y = 728

    while True:
        # 获取事件，比如按键等
        for event in pygame.event.get():

            # 绑定图片到窗口
            screen.blit(bg, (0, 0))

            # 绑定玩家飞机到窗口
            screen.blit(hero.image, (hero.x, hero.y))

            # 刷新图片
            pygame.display.update()

            # 判断是否是点击了退出按钮
            if event.type == QUIT:
                print("exit")
                exit()
            # 判断是否是按下了键
            elif event.type == KEYDOWN:
                # 检测按键是否是a或者left
                if event.key == K_a or event.key == K_LEFT:
                    print('left')
                    x -= 10

                # 检测按键是否是d或者right
                elif event.key == K_d or event.key == K_RIGHT:
                    print('right')
                    x += 10

                # 检测按键是否是空格键
                elif event.key == K_SPACE:
                    print('space')

# time.sleep(60)


if __name__ == '__main__':
    main()
