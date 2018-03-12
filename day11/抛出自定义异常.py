"""
测试抛出自定义异常
编写代码，自定义一个异常类，如果两个数相除，余数不为零则抛出自定义异常。
"""


class Result(Exception):
    pass


def chu(a, b):
    try:
        if b == 0:
            raise Result()
    except Result as chushu:
        print('捕捉到异常', chushu)

    else:
        print(a/b)

chu(1, 0)
