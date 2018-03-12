"""
类创建对象

"""


class People:
    def info(self):
        print('%s 的公司是 %s' %(self.name, self.company))


mayun = People()
mayun.name = '马云'
mayun.company = '阿里巴巴'
mayun.info()


wangjianglin = People()
wangjianglin.name = '王健林'
wangjianglin.company = '万达集团'
wangjianglin.info()
