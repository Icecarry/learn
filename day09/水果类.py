"""
创建水果类，打印颜色
"""


class Fruit:
    def print_color(self):
        print("颜色是 %s" % (self.color))


apple = Fruit()
apple.color = "red"
apple.print_color()

orange = Fruit()
orange.color = "yellow"
orange.print_color()

watermelon = Fruit()
watermelon.color = "green"
watermelon.print_color()
