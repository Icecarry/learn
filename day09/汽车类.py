"""
定义一个汽车类，
并在类中定义一个move方法打印'汽车在移动'，
然后分别创建BMW_X9、AUDI_A9对象，
并添加颜色、型号等属性，然后打印出属性值,
最后调用move方法。(注意：不要使用 init 方法)
"""


class Car:
    def move(self, name, color, model):
        self.name = name
        self.color = color
        self.model = model
        print("%s 的颜色为 %s ,型号为 %s" % (self.name, self.color, self.model))
        print('汽车在移动')


BMW_X9 = Car()
BMW_X9.move('BMW', '白色', 'X9')


AUDI_A9 = Car()
AUDI_A9.move('AUDI', '黑色', 'A9')
