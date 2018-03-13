"""
3. 匹配用一个空格分隔的任意一对单词，比如，名和姓
import re
res = re.findall(r'\w* \w*','michael jackson').group()

"""
import re


def main():
    s = 'hello world ggg!'
    res = re.findall(r'\w* \w*', s)
    print(res)


if __name__ == '__main__':
    main()
