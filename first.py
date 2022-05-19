class A:
    y = "Y"

    def __init__(self, x):
        self.x = x

    def f_a(self):
        pass

    def f_b(self):
        pass

    @staticmethod
    def f_c():
        pass


m = A(2)
n = A(3)

print(m.x, n.x)
print(m.y, n.y)
