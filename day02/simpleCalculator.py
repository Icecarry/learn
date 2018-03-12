#设计简易计算器，进行进本加减乘除

#用户输入第一个数字
#用户输入一个操作符
#用户输入第二个数字
#进行计算

num1 = int(input("请输入第一个数字："))
ope = input("请输入一个操作符(+ - * /)：")
num2 = int(input("请输入第二个数字："))
#计算加法
if ope == '+':
    sum = num1 + num2
    print(sum)
#计算减法
elif ope == '-':
    sub = num1 - num2
    print(sub)
#计算乘法
elif ope == '*':
    mult = num1 * num2
    print(mult)
#计算除法
elif ope == '/':
    if num2 == 0:
        print("输入不能为0")
    else:
        div = num1 / num2
        print(div)
#输入有误类
else:
    print("操作符输入错误")