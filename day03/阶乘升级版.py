'''
从键盘获取一个数字，然后计算它的阶乘，
例如输入的是3，那么即计算3!的结果，并输出
'''

#输入数字
i = int(input("请输入想要计算的阶乘数："))
start = 1
res = 1
if i == 0:
    print("0的阶乘是： 1")
else:
    while start <= i:
    #    print(i)
        res *= start
        start += 1
    print("%d 的阶乘结果为：%d" % (i, res))