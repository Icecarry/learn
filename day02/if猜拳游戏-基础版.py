# 猜拳游戏

#玩家猜拳
#电脑猜拳
#比较得出输赢

player = int(input("请出拳（剪刀 0，石头 1，布 2）："))
computer = 1
#比较玩家和电脑
if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
    print("玩家获胜")
elif (player == computer):
    print("平局")
else:
    print("电脑获胜")

