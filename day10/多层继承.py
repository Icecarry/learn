class Animal(object):
    # def __init__(self):
    #     self.age = 10
    def eat(self):
        print('吃肉')


class BuRu(Animal):
    pass
    # def eat(self):
    #     print('吃鱼')
    # def __init__(self):
    #     self.name = 'mao'
    #     super().__init__()


class Cat(BuRu):
    def eat(self):
        print('chimi')
        # Animal.eat(self)  #  指定调用的父类
        # BuRu.eat(self)
        super(Cat, self).eat()  # 往上寻找上一级父类的方法

cat = Cat()
# print(cat.)
cat.eat()


