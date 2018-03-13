# 1. 计算一个方法被调了多少次
# 2. 计算函数的执行时间,time.sleep(1)
num = 0

def set_fun(func):

    def call_fun(*args,**kwargs):
        global  num
        num += 1
        print(num)
        #后期会写到数据 库中
        return func(*args,**kwargs)
    return call_fun


@set_fun
def open_url():
    print("打开")

open_url()
open_url()
open_url()
open_url()

##这个是第一种
def set_fun(func):
    num = 0
    def call_fun(*args,**kwargs):

        #去执行后去添加值
        nonlocal num
        num += 1
        print(num)

        return func(*args,**kwargs)
    return call_fun

@set_fun    # open_url = set_fun(open_url)
def open_url():
    print("打开")

open_url()
open_url()
open_url()
open_url()

