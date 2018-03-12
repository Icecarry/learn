"""
地瓜要有烤熟的程度，要有表示烤没烤好，要配调料，
方法 烤
"""
import random


class Sweetpotato:
    def __init__(self):
        self.cooklevel = 0  # 烤熟的等级
        self.cookstring = '生的'  # 烤没烤好
        self.condiments = ['辣椒酱', '甜面酱', '沙拉酱', '番茄酱', '芥末酱']  # 调料的种类

    # 靠番薯
    def auto_cook(self, time):
        while True:
            if self.cooklevel <= 5:
                self.cooklevel += time
            elif self.cooklevel > 8:
                self.cooklevel -= 1
            else:
                break
        # 判断成熟度
        if self.cooklevel >= 0 and self.cooklevel <= 3:
            self.cookstring = '是生的'
        elif self.cooklevel <= 5:
            self.cookstring = '半生不熟的'
        elif self.cooklevel <= 8:
            self.cookstring = '已经烤好了'
        else:
            self.cookstring = '已经烤成碳了'

    # 添加佐料
    def auto_addcondiments(self):
        # 添加到列表
        ran = random.randint(0, 4)
        self.item = self.condiments[ran]
        # self.condiments.append(item)

    def __str__(self):
        return '地瓜烤熟等级为 %d, 它 %s,它加了 %s' % (self.cooklevel, self.cookstring, self.item)

hongshu = Sweetpotato()
hongshu.auto_cook(4)
hongshu.auto_addcondiments()
print(hongshu)