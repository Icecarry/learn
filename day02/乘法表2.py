# 写出九九乘法表

# 用for写

# i 代表行数
# i = 1

for i in range(1, 10):
    j = 1
    for j in range(1, i + 1):
        print("%s*%s=%-3s" % (j, i, i * j), end='')
    print("\n")

