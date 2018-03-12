"""
判断闰年

"""
# 用户输入日期
# date = input('请输入一个有效的日期：')
# year = int(date[0:4])
# month = int(date[4:6])
# day = int(date[6:])
# noRunNina = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# runNian = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# # 判断是否有效
# if len(date) != 8:
#     print('日期输入无效!')
# else:
#     if month < 1 or month > 12:
#         print('月份输入无效。')
#     else:
#         if year % 4 != 0:
#             if day > noRunNina[month]:
#                 print('天数输入有误。')
#             else:
#                 print('输入正确')
#         else:
#
#             if year % 100 == 0 and year % 400 != 0:
#                 if day > noRunNina[month]:
#                     print('天数输入有误。')
#                 else:
#                     print('输入正确')
#             else:
#                 if day > runNian[month]:
#                     print('天数输入有误。')
#                 else:
#                     print('输入正确')


def runina(year):
    if year % 4 != 0:
        return '不是润年。'
    else:
        if year % 100 == 0 and year % 400 != 0:
            return '不是闰年。'
        else:
            return '是闰年！'


year = int(input("请输入一个年份："))
# runNian(year1)
panduan = runina(year)
print(panduan)