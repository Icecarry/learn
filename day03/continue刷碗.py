'''
写程序完成以下功能，晚饭后你负责刷掉家里的 10 个碗，
当刷到第 5 个碗时跳过不刷，直接开始刷第 6 个碗
'''

#碗从第十个开始刷
i = 10


while i > 0:
    if i == 6:
        print("停止刷碗！")
        i -= 1
        continue

    print("刷碗，不要停！%d" % i)
    i -= 1
