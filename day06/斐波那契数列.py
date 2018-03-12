"""
使用函数求前n个数的斐波那契数列。n为函数参数
"""

# 自加
# def zi_jia(num):


def foc(n):
    count = 0
    sum1 = 0
    after = 1
    before = 1

    if n == 1:
        sum1 = 1
    elif n == 2:
        sum1 = 1
    elif n > 2:
        while count < n - 2:
            after, before = after + before, after
            # i = sum1 + i
            sum1 = after
            count += 1
    return sum1


# 不用函数
n = int(input("n:"))
count = 1
foc_list = []
while count <= n:
    num = foc(count)
    foc_list.append(num)
    count += 1
print(foc_list)


# print(sum1)

