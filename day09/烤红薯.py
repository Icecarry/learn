"""
地瓜要有烤熟的程度，要有表示烤没烤好，要配调料，
方法 烤
"""


class Sweetpotato:
    def __init__(self):
        self.cooklevel = 0  # 烤熟的等级
        self.cookstring = '生的'  # 烤没烤好
        self.condiments = []  # 调料的种类

    # 靠番薯
    def cook(self, time):
        self.cooklevel += time
        # 判断成熟度
        if self.cooklevel >= 0 and self.cooklevel <=3:
            self.cookstring = '是生的'
        elif self.cooklevel <= 5:
            self.cookstring = '半生不熟的'
        elif self.cooklevel <= 8:
            self.cooklevel = '已经烤好了'
        else:
            self.cooklevel = '已经烤成碳了'

    # 添加佐料
    def addcondiments(self, item):
        # 添加到列表
        self.condiments.append(item)

    def __str__(self):
        return '地瓜烤熟等级为 %d, 它 %s,它加了 %s' % (self.cooklevel, self.cookstring, self.condiments)

hongshu = Sweetpotato()
hongshu.cook(2)
hongshu.cook(2)
hongshu.addcondiments('辣椒酱')
print(hongshu)