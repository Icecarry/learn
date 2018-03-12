# 房子类
class Home:
    def __init__(self, area):
        # 初始化房子的大小
        self.area = area  # 房子的大小
        # self.beds = []  # 床的列表

    def __str__(self):
        """返回房子的描述信息"""
        # 把床的名字提取成一个字符串列表
        # self.beds如果直接打印看到的是对象元素的内存地址，需要转成字符串列表才能提取

        # names = []
        # for bed in self.beds:
        #     names.append(bed.name)
        return '房间的大小为：%d平米' % self.area

    def add_item(self, bed):
        """添加一张床到房间"""
        if self.area >= bed.area:
            # self.beds.append(bed)
            self.area -= bed.area
        else:
            print('剩余空间不足，无法放入 %s' % bed.name)


# 床类
class Bed:
    def __init__(self, name, area):
        """初始化床的信息"""
        self.name = name  # 床的名字
        self.area = area  # 床的大小

    def __str__(self):
        """返回床的信息"""
        return '%s 的大小为: %d' % (self.name, self.area)


# 创建房子
home = Home(300)


# 放置床
xms = Bed('席梦思', 4)
print(xms)


# 把床放到房间里
home.add_item(xms)
print(home)
