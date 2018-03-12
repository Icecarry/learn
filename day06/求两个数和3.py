# 编写一段代码，求两个数的和


def sum1(num1, num2):
    """ 用来求和 """
    sum2 = num1 + num2
    return sum2


num1 = int(input('输入数字1：'))
num2 = int(input('输入数字2：'))

print(sum1(num1, num2))

help(sum1)
