# 猜拳游戏

#玩家猜拳
#电脑猜拳
#比较得出输赢

#电脑随机出拳
import random


#玩家赢的次数
win = 0
print("赢三次才能退出游戏")
#死循环
while True:
    player = int(input("请出拳（剪刀 0，石头 1，布 2）："))
    computer = random.randint(0,2)
    print(computer)
    #比较玩家和电脑
    if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
        print("玩家获胜")
        win += 1
    elif (player == computer):
        print("平局")
    else:
        print("电脑获胜")

    #判断玩家是否赢三次
    if win >= 3:
        break
