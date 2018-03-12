# 编写一段代码，求1-100之间所有整数的和


# def sum1(m, n):
# return summer


# sum1(1, 50)
# 用户输入
num1 = int(input("请输入起始数："))
num2 = int(input("请输入结束的数："))
# print("%d - %d 之间的所有整数和为：" % (num1, num2), sum1(num1, num2))

# 运用循环累加
summer = 0
for x in range(num2 + 1):
    if x >= num1:
        summer += x
    else:
        continue
print(summer)
