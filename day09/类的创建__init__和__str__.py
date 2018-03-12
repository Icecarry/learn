"""
类创建对象

"""


class People:
    def __init__(self, name, company):
        self.name = name
        self.company = company
        # print('%s 的公司是 %s' % (self.name, self.company))

    def __str__(self):
        return '%s 的公司是 %s' % (self.name, self.company)
    # def info(self):
    #     print('%s 的公司是 %s' %(self.name, self.company))


mayun = People('马云', '阿里巴巴')
print(mayun)
# mayun.name = '马云'
# mayun.company = '阿里巴巴'
# mayun.info()
#
#
wangjianlin = People('王健林', '万达集团')
print(wangjianlin)
# wangjianglin = People()
# wangjianglin.name = '王健林'
# wangjianglin.company = '万达集团'
# wangjianglin.info()
