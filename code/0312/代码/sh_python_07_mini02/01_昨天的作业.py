import  time
#时间差,程序执行前程序执行后加时间
def set_fun(func):
    def call_fun(*args,**kwargs):
        print(time.time())
        func1 = func(*args, **kwargs)
        print(time.time())
        # 时间戳 可以表示唯一值,多数用在加密
        return func1
    return call_fun

@set_fun
def test():
    print("test")
    time.sleep(1)
    #5秒的就可以考虑了

test()