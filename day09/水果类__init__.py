"""
创建水果类，打印颜色
"""


class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        print("%s 的颜色是 %s" % (self.name, self.color))

    # def print_color(self):
    #     print("颜色是 %s" % (self.color))


apple = Fruit('apple',"red")
# apple.color = "red"
# apple.print_color()

orange = Fruit('orange', 'yellow')
# orange.color = "yellow"
# orange.print_color()

watermelon = Fruit('watermelon', 'green')
# watermelon.color = "green"
# watermelon.print_color()
