"""
递归函数求n的阶乘
"""


def func1(num):
    if num == 1:
        return 1
    else:
        res = num * func1(num - 1)
    return res


x = int(input("输入要计算的阶乘数："))
jc = func1(x)
print("阶乘为：", jc)
