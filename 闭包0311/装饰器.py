# 这是装饰器


def test_fun(func):
    def call_fun(*args, **kwargs):
        # 使用修饰器，万能修饰器
        return func(*args, **kwargs)

    return call_fun


@test_fun
def test(*args, **kwargs):
    return args, kwargs
    # print('123')


print(test(123, 345, a=5))
