'''
把关卡2-练习1中的题1增加一个功能，
要求统计输入的字符串中不同字符的个数，
使用字典存储，并打印出来
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

#字典存储不同字符串
# print(string)
sta = {}
for tmp in string:
    num = sta.get(tmp, 0)

    if num == 0:
        sta[tmp] = 1
    else:
        sta[tmp] += 1

print(sta)
