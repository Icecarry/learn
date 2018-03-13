"""
5. 匹配合法的ip地址
??
import re
mystr = '10.16.20.3'
print(re.match(r"^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]{1,2})(\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]{1,2})){3}$",mystr).group())
"""
import re


def main():
    ip = input("请输入ｉｐ地址：")
    rule = r'^25[0-5]|2[0-4][0-9]|[0-1]?[0-9]?[0-9](\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]?[0-9])){3}'

    res = re.match(rule, ip)
    if res:
        print(res.group())
    else:
        print('不是ｉｐ地址')


if __name__ == '__main__':
    main()
