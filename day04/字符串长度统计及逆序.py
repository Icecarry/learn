'''
完成字符串的长度统计以及逆序打印
    * 设计一个程序，要求只能输入长度低于31的字符串，否则提示用户重新输入
    * 打印出字符串长度
    * 使用切片逆序打印出字符串
'''

while True:
    # 用户输入，且字符串长度小于31
    string = input("请输入字符串，长度请低于31：")
    #把字符串存放在列表里方便排序
    # string_list = []

    # 判断长度是否低于31
    length = len(string)
    if length < 32:
        print("字符串长度为 %d" % length)
        print(string[::-1])
        break
    else:
        print("超出长度，请重新输入！")
        continue