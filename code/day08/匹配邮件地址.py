"""
6. 匹配所有合法的电子邮件地址(先写出一个限制比较宽松的正则表达式，然后尽可能加 强限制条件，但要保证功能的正确性)。
import re


def main():
    ""匹配合法的邮箱名主逻辑""
    # 获取邮箱列表
    email_list = ["291470550@qq.com","123456@163.com","wangzirangy11@gmail.com"]
    # 遍历邮箱列表，匹配出满足条件的邮箱
    for email in email_list:
        res = re.match(r'[\da-zA-Z_]{8,20}@(qq|163|gmail)\.com$',email)
        if res:
            print("满足邮箱命名条件：%s" % res.group())
        else:
            print("不满足邮箱命名条件：%s" % email)

if __name__ == '__main__':
    main()
"""
import re


def main():
    mail = input('请输入邮件地址：')
    rule = r'[a-zA-Z0-9_]{8,20}@(gmail|qq|163)\.com$'

    res = re.match(rule, mail)
    if res:
        print('满足邮箱命名条件：%s' % res.group())
    else:
        print('不满足邮箱命名条件：%s' % mail)


if __name__ == '__main__':
    main()