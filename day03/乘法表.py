#使用循环嵌套打印九九乘法表

i = 1
while i <= 9:
    j = 1
    while j <= i:
        n = i
        k = j * n
        print("%s * %s = %s  " % (j, n, k), end = '')
        j += 1

    print("\n")
    i += 1