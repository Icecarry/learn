#coding=utf-8

#每行打印与行数相同的 *
#定义行数 i
i = 1

#如果i小于5行循环
while i <= 5:
    #定义个数
    j = 1
    while j <= i:
        print("* ",end = '')
        j += 1
    print("\n")
    i += 1