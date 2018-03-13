"""
7. 将一篇中文文章中的电子邮件地址替换为你自己的电子邮件地址
import re


def main():
    ""替换一篇文章中的所有邮箱地址为池281470550@qq.com主逻辑""
    # 导入文章
    with open("file.txt","r") as file:
        content = file.read()

    # 匹配替换邮箱
    res = re.sub(r'[0-9a-zA-Z_]{8,20}@(qq|163|gmail)\.com','281470550@qq.com',content)

    # 写入新的文本中
    with open("file[替换后].txt","w") as res_file:
        res_file.write(res)


if __name__ == '__main__':
    main()
"""
import re


def main():
    with open('file.txt') as file:
        content = file.read()

    rule = r'[a-zA-Z0-9_]{8,20}@(gmail|qq|163)\.com'
    replace = '281470550@qq.com'
    res = re.sub(rule, replace, content)
    print(res)

    with open('file[替换].txt','w') as file:
        file.write(res)


if __name__ == '__main__':
    main()


# import re
#
#
# def main():
#     """替换一篇文章中的所有邮箱地址为池281470550@qq.com主逻辑"""
#     # 导入文章
#     with open("file.txt","r") as file:
#         content = file.read()
#
#     # 匹配替换邮箱
#     res = re.sub(r'[0-9a-zA-Z_]{8,20}@(qq|163|gmail)\.com','281470550@qq.com',content)
#
#     # 写入新的文本中
#     with open("file[替换后].txt","w") as res_file:
#         res_file.write(res)
#
#
# if __name__ == '__main__':
#     main()
