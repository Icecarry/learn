"""
2. 查找所有的单词
```
hello world ha ha
```
```
print(re.findall(r'\w+',mystr))
```
"""
import re


def main():
    file = open('匹配网站.py')
    connect = file.read()
    file.close()

    res = re.findall(r'\w*',connect)
    print(res)

if __name__ == '__main__':
    main()
