# coding = utf-8
# __author__ = 'wang wei'
import math

# 实现一个优先级队列
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.hypot(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "Point({0.x!r},{0.y!r})".format(self)

    def __str__(self):
        return "({0.x!r},{0.y!r})".format(self)


class Circle(Point):
    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    # @property
    def edge_distance_from_origin(self):
        return abs(self.distance_from_origin() - self.radius)

    # @property
    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

    def __eq__(self, other):
        return self.radius == other.radius and super().__eq__(other)

    def __repr__(self):
        return "Circle({0.radius!r},{0.x!r},{0.y!r})".format(self)

    def __str__(self):
        return repr(self)

        # cookbook


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
    def give_raise(self, percent, bonus=.10):
        Person.give_raise(self, percent + bonus)


if __name__ == "__main__":
    """
        a = Point()
        print(a.__repr__())
        b = Point(3, 4)
        print(b.distance_from_origin())
        b.x = -19
        print(b.__str__())

        print(a == b, a != b)
        print("=======================")
        print(str(a))
        print("========================")

        print(dir(Circle))
    ==========================
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print(bob.name.split()[-1])
    sue.pay *= 1.10
    print(sue.pay)
    ==========================
    """
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=10000)
    print(bob.name)
    print(sue.name, sue.pay)
    print(bob.last_name(), sue.last_name())
    sue.give_raise(.10)
    print(sue.pay)
    print(sue)
