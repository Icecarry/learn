# 闭包


def test_fun(func):
    def call_fun():
        print('这是闭包')
        func()

    return call_fun


def test():
    print('test')


test = test_fun(test)
test()
