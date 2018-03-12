#coding=utf-8

#检测身高

#输入身高
Hight = input("请输入身高：")

#if-else判断语句
if int(Hight) <= 150:
    print("免票进入。")
else:
    print("进园请买票！")