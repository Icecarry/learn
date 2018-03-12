"""
使用函数求前n个数的斐波那契数列。n为函数参数
"""

# 自加
# def zi_jia(num):


def foc(n):
    # res = 1
    # foc(1) = 1
    if n == 1:
        res = 0
        return res
    elif n == 2:
        res = 1
        return res
    elif n > 2:
        res = foc(n - 1) + foc(n - 2)
        return res


# 调用函数
n = int(input("n:"))
# count = 0
num = 1
foc_list = []
while num <= n:
    foc(num)
    foc_list.append(foc(num))
    num += 1

print(foc_list)


# print(sum1)

