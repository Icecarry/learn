"""
编写一个函数验证哥德巴赫的猜想：
任何一个充分大的偶数（大于等于6）总可以表示成两个素数之和-----
要求：将6-100之间的偶数，都用两个素数之和去表示
"""


# 求素数
def prime(num):
    if num > 2:
        for x in range(2, num):
            if num % x != 0:
                continue
            else:
                return
        return num
    elif num == 2:
        return 2


# a = prime(5)
# print(a)


a = []
for m in range(2, 101):
    if prime(m) is None:
        continue
    else:
        a.append(prime(m))
print(a)

for x in range(6, 101, 2):
    for i in a:
        for j in a:
            if x == i + j:
                if i <= j:
                    print("%d = %d + %d" % (x, i, j))
