"""
判断有效日期
用户可以输入"20170327"等三种格式的日期
判断是否是有效日期，如"20170229"不是有效日期，
"20171345"不是有效日期
"""


# 年月日转换
def con(date):
    year = int(date[0:4])
    month = int(date[4:6])
    day = int(date[6:])
    return year, month, day


# 判断是否为闰年
def leap():
    year = con(date)[0]
    if year % 4 != 0:
        return 0
        # return '不是润年。'
    else:
        if year % 100 == 0 and year % 400 != 0:
            return 0
            # return '不是闰年。'
        else:
            return 1
            # return '是闰年！'


# 月份判断
def mon_jud():
    month = con(date)[1]
    if month < 1 or month > 12:
        print('月份输入无效。')
    else:
        dat_jud()


# 日期判断
def dat_jud():
    day = con(date)[2]
    month = con(date)[1]
    jud = leap()
    if jud == 1:
        if day > runNian[month]:
            print('天数输入有误。')
        else:
            print('输入正确')
    else:
        if day > noRunNina[month]:
            print('天数输入有误。')
        else:
            print('输入正确')


noRunNina = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
runNian = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 用户输入日期
date = input('请输入一个有效的日期：')
con(date)

# 判断是否有效
if len(date) != 8:
    print('日期输入无效!')
else:
    mon_jud()
    # if month < 1 or month > 12:
    #     print('月份输入无效。')
    # else:
    #     if year % 4 != 0:
    #         if day > noRunNina[month]:
    #             print('天数输入有误。')
    #         else:
    #             print('输入正确')
    #     else:
    #
    #         if year % 100 == 0 and year % 400 != 0:
    #             if day > noRunNina[month]:
    #                 print('天数输入有误。')
    #             else:
    #                 print('输入正确')
    #         else:
    #             if day > runNian[month]:
    #                 print('天数输入有误。')
    #             else:
    #                 print('输入正确')

