"""
8. 取出属性data-original对应的url
```
 <img data-original="https://rpic.douyucdn.cn/z1609/07/15/478748_160907150833.jpg" src="https://rpic.douyucdn.cn/z1609/07/15/478748_160907150833.jpg" style="display: block;">
```
import re


# 获取文件内容
file ='''
 <img data-original="https://rpic.douyucdn.cn/
 z1609/07/15/478748_160907150833.jpg"
 src="https://rpic.douyucdn.cn/z1609/07/15/478748_160907150833.jpg"
 style="display: block;">
'''

# 提取出所有url
url_list = re.findall(r'https://.*?\.jpg',file,re.S)

# 打印出所有url
print(url_list)
"""
import re


def main():
    file = '''
 <img data-original="https://rpic.douyucdn.cn/
 z1609/07/15/478748_160907150833.jpg"
 src="https://rpic.douyucdn.cn/z1609/07/15/478748_160907150833.jpg"
 style="display: block;">
'''

    rule = r'data-original=\"https://.*?\"'
    res = re.findall(rule, file, re.S)
    print(res)


if __name__ == '__main__':
    main()
