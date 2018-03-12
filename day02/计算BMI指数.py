#输入身高，体重，根据公式计算BMI指数
#公式
#体重（kg） / 身高（m）的平方 = BMI

#定义变量，输入身高体重
height = float(input("请输入身高（cm）："))
weight = float(input("请输入体重（kg）："))

#代入公式
BMI = weight / ((height/100) ** 2)
print(BMI)

if BMI < 18.5:
    print("过轻")
elif 18.5 <= BMI < 25:
    print("正常")
elif 25 <= BMI < 28:
    print("过重")
elif 28 <= BMI <=32:
    print("肥胖")
else:
    print("严重肥胖")

