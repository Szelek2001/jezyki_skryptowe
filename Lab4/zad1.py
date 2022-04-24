import math
import random
import string


class MyClass:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @property
    def c(self):
        return self._c

    @a.setter
    def a(self, a):
        self._a = a

    @b.setter
    def b(self, b):
        if isinstance(b, (int, float)):
            if b > 0:
                self._b = b
            else:
                raise ValueError("Liczba musi być dodatnia")
        else:
            raise TypeError("Int lub Float")

    @c.setter
    def c(self, c):
        if isinstance(c, (int, float)):
            self._c = c
        else:
            raise TypeError("Int lub Float")

    @a.deleter
    def a(self):
        del self._a

    @b.deleter
    def b(self):
        del self._b

    @c.deleter
    def c(self):
        del self._b

    def printA(self):
        print(self._a)

    def printBSQRT(self):
        print(math.sqrt(self._b))

    def printmultC(self, numb):
        print(self._c * numb)

    def setAttrValue(self, attr, value):
        if attr not in self.__dict__.keys():
            raise ValueError

        setattr(self, attr, value)


def printObject(obj):
    attr = obj.__dict__
    for key, value in attr.items():
        print(f'{key} : {value}', end='\t')
    print()


myClassObjects = [MyClass(x, x + 1, x + 100) for x in range(4)]

myClassObjects[0].printA()
myClassObjects[1].printBSQRT()
myClassObjects[2].printmultC(30)

for x in myClassObjects:
    printObject(x)

newAttr = 'd'
newAttrValue = 2137

for x in myClassObjects:
    setattr(x, newAttr, newAttrValue)
    newAttr = random.choice(string.ascii_letters)
    newAttrValue += 10

for x in myClassObjects:
    printObject(x)

try:
    myClassObjects[0].setAttrValue('a', 100)
    myClassObjects[1].setAttrValue('x', 100)
    myClassObjects[2].setAttrValue('y', 100)
    myClassObjects[3].setAttrValue('n', 100)
except ValueError:
    print("No given attribute")

for x in myClassObjects:
    printObject(x)


