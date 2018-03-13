"""
4. 匹配所有合法的Python标识符
import re
list = ["abcd123","123abc","_123","123abc?."]
for x in list:
    res = re.match(r'[a-zA-Z_]\w*',x)
    if res:
        print("是合法的python标识符：%s" % res.group())
    else:
        print("不是合法的python标识符：%S" % x)
"""
import re


def main():
    str = input('请输入标识符：')
    res = re.match(r'[a-zA-Z_][a-zA-Z0-9_]*',str)
    if res:
        print('%s 是标识符' % res.group())
    else:
        print('%s 不是标识符' % str)


if __name__ == '__main__':
    main()