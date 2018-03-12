#coding=utf-8

#score = 77


while (1):
    a = input("请输入分数：")
    score = int(a)
    if score>=90 and score<=100:
        print('本次考试，等级为A')
    elif score>=80 and score<90:
        print('本次考试，等级为B')
    elif score>=70 and score<80:
        print('本次考试，等级为C')
    elif score>=60 and score<70:
        print('本次考试，等级为D')
    elif score>=0 and score<60:
        print('本次考试，等级为E')

    b = input("请确认是否继续：Y/N")
    if b == "N":
        break