#测试break和continue

#普通循环
name = 'itheima'

for x in name:
    print('----')
    print(x)
else:
    print("==for循环过程中，如果没有执行break退出，则执行本语句==")


name = 'itheima'

for x in name:
    print('----')
    if x == 'e':
        break
    print(x)
else:
    print("==for循环过程中，如果没有执行break退出，则执行本语句==")