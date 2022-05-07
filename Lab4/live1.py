class TWO():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def mult(self):
        return self.a * self.b


class WINCEJ(TWO):
    def __init__(self, a, b, *args, **kwargs):
        super().__init__(a, b)
        self.c = 0
        for argu in args:
            self.c += argu
        self.mama = 1
        for keys, number in kwargs.items():
            if (keys == "mama"):
                self.mama = self.mama * number
            else:
                self.c = self.c * number

    def mult(self):
        return self.a * self.b * self.c

    def mult_mam(self):
        return self.mama


a = TWO(10, 10)
b = WINCEJ(10, 5, 5, 5, 5, 5, mama=2, tata=5, mam=5)
print(a.mult())
print(b.mult())
print(b.mult_mam())
