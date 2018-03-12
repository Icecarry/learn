# """
# 终端接收参数
# """
#
#
# import sys
#
#
# # 打印传进来的参数
# print(sys.argv)
#
# # 传参
# a = int(sys.argv[1])
# b = int(sys.argv[2])
#
# print('相加的结果为：%d' % (a + b))
#

class Person(object):
    num = 1


p1 = Person()
p1.num = 2
print(p1.num)
print(Person.num)
