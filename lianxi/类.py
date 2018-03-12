class Cat:
    def talk(self):
        self.age = 18
        # print('age %s' % self.age = 18)
        print('talk %s' % self.name)


tom = Cat()
tom.name = 'xiaobao'
tom.talk()
print(tom.age)

jac = Cat()
print(jac.age)
# jac.talk()
