"""
飞机大战，加载背景
"""
import pygame
import time
from pygame.locals import *


# 飞机类
class HeroPlane(object):

    def __init__(self, screen):
        # 初始化飞机参数
        self.x = 190
        self.y = 728

        # 初始化窗口
        self.screen = screen

        # 飞机图片路径
        image_path = 'feiji/hero1.png'
        self.image = pygame.image.load(image_path)

        # 飞机里子弹列表
        self.bulletlist = []

    # 显示飞机
    def display(self):

        dellet_bullet = []

        self.screen.blit(self.image, (self.x, self.y))

        for bullet in self.bulletlist:
            bullet.display()
            bullet.move()

            if bullet.remove():
                dellet_bullet.append(bullet)
        for bullet in dellet_bullet:
            self.bulletlist.remove(bullet)

    # 飞机移动
    def moveleft(self):
        self.x -= 10

    def moveright(self):
        self.x += 10

    # 飞机射击
    def shoot(self):
        new_bullet = Bullet(self.x, self.y, self.screen)
        self.bulletlist.append(new_bullet)


# 飞机类
class EnemyPlane(object):

    def __init__(self, screen):
        # 初始化飞机参数
        self.x = 0
        self.y = 10

        # 初始化窗口
        self.screen = screen

        # 飞机图片路径
        image_path = 'feiji/enemy0.png'
        self.image = pygame.image.load(image_path)

        # 飞机里子弹列表
        self.bulletlist = []

        self.oritation = 'right'

    # 显示飞机
    def display(self):

        dellet_bullet = []

        self.screen.blit(self.image, (self.x, self.y))

        # for bullet in self.bulletlist:
        #     bullet.display()
        #     bullet.move()
        #
        #     if bullet.remove():
        #         dellet_bullet.append(bullet)
        # for bullet in dellet_bullet:
        #     self.bulletlist.remove(bullet)


    def automove(self):

        if self.x <= 0:
            self.oritation = 'right'
        elif self.x >= 480 - 55:
            self.oritation = 'left'

        if self.oritation == 'right':
            self.moveright()
        elif self.oritation == 'left':
            self.moveleft()

    # 飞机移动
    def moveleft(self):
        self.x -= 10

    def moveright(self):
        self.x += 10

    # 飞机射击
    def shoot(self):
        new_bullet = Bullet(self.x, self.y, self.screen)
        self.bulletlist.append(new_bullet)



# 子弹类
class Bullet(object):

    # 子弹初始化
    def __init__(self, plan_x, plan_y, screen):
        self.x = plan_x + 39
        self.y = plan_y - 22

        image_path = 'feiji/bullet.png'
        self.image = pygame.image.load(image_path)
        self.screen = screen

    # 子弹移动
    def move(self):
        self.y -= 10

    # 子弹显示
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    # 移除子弹
    def remove(self):
        return self.y < 0

    def __del__(self):
        print('子弹被移除')


# 键盘输入
def key_control(hero):

    # 获取事件，比如按键等
    for event in pygame.event.get():

        # 判断是否是点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        # 判断是否是按下了键
    key_buf = pygame.key.get_pressed()
    # if key_buf[pygame.KEYDOWN] == 1:
    # 检测按键是否是a或者left
    if key_buf[pygame.K_a] == 1 or key_buf[pygame.K_LEFT] == 1:
        print('left')
        # move_x = -1
        hero.moveleft()

    # 检测按键是否是d或者right
    if key_buf[pygame.K_d] == 1 or key_buf[pygame.K_RIGHT] == 1:
        print('right')
        # move_x = 1
        hero.moveright()

    # 检测按键是否是空格键
    if key_buf[pygame.K_SPACE] == 1:
        print('space')
        hero.shoot()
    # elif key_buf[pygame.K_SPACE] == 0:
    #     pass


def main():
    # 创建窗口
    screen = pygame.display.set_mode((480, 852), 0, 32)

    # 加载图片
    bg = pygame.image.load('feiji/background.png')

    # 加载玩家飞机
    hero = HeroPlane(screen)

    # 加载敌人飞机
    enemy = EnemyPlane(screen)
    while True:
        # 绑定图片到窗口
        screen.blit(bg, (0, 0))

        # 绑定玩家飞机到窗口
        hero.display()

        enemy.display()
        enemy.automove()

        # 键盘输入
        key_control(hero)

        # 刷新图片
        pygame.display.update()

        time.sleep(1/24)


if __name__ == '__main__':
    main()
