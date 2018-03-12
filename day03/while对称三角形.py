'''
使用while，完成以下图形的输出
 ```
 *
 * *
 * * *
 * * * *
 * * * * *
 * * * *
 * * *
 * *
 *
 ```
'''

#每行打印行数的星号
#行数
i = 1

while i < 10:
#打印个数
    if i <= 5:
        j = 1
        while j <= i:
            print("*", end=' ')
            j += 1
    else:
        j = 1
        while j <= (10 - i):
            print("*", end=' ')
            j += 1
    print()
    i += 1
