# 匹配０－９９之间的数字
import re


def main():
    str = input("请输入数字０－９９：")
    rule = r'[0-9]?[0-9]'
    res = re.match(rule, str)
    print(res.group())


if __name__ == '__main__':
    main()
