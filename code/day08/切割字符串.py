"""
1.切割字符串“info:xiaoZhang 33 shandong”
import re
res = re.split(r':| ','info:xiaoZhang 33 shandong')
print(res)

"""
import re


def main():
    str = 'info:xiaoZhang 33 shandong'
    rule = r':| '
    res = re.split(rule,str)
    print(res)


if __name__ == '__main__':
    main()
