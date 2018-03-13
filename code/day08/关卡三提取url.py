"""
3.str = ""<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display: inline;">""
提取其中的url
import re
res = re.findall(r'http://.*?\.jpg',str,re.S)
print(res)
"""
import re


def main():
    str = """
            <img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg"
            src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg"
            style="display: inline;">
            """
    rule = r'https://.+\.jpg'

    res = re.findall(rule, str)
    print(res)


if __name__ == '__main__':
    main()
