"""
定义一个不定长参数的函数，
并在函数中打印出所有参数及其类型，
统计传入参数的个数
"""


# 定义一个不定长参数
def cou1(num, *args, **kw_args):
    print('a = %d' % num)
    print('args: ')
    print(args)
    print('kw_args: ')
    print(kw_args)


args1 = [2, 3, 4, 5]
kw_args1 = {'a': '1', 'b': '2', 'c': '3'}
# cou1(1, *args1, **kw_args1)
cou1(1, *args1, a=1, b=2, c=3)



