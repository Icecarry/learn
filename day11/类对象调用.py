class Func1(object):
    ls = '1'

    @staticmethod
    def eat():
        s = Func1.ls
        print(s)

    @classmethod
    def eat2(cls):
        print(cls.ls)


fu = Func1()
fu.eat()
fu.eat2()
print(Func1.ls)
