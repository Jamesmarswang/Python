# coding = utf-8
# __author__ = 'wang wei'


class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):
        return '[Person:%s,%s]' % (self.name, self.pay)


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def give_raise(self, percent, bonus=0):
        Person.give_raise(self, percent + bonus)


class Manager2:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)

    def give_raise(self, percent, bonus=.10):
        self.person.give_raise(percent + bonus)

    def __getattr__(self, attr):
        return getattr(self.person, attr)

    def __str__(self):
        return str(self.person)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=10000)
    print(bob, sue)
    print(bob.last_name(), sue.last_name())
    sue.give_raise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.give_raise(.10)
    print(tom.last_name())
    print(tom)
