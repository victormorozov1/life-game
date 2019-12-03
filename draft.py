import copy


class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b


q = A(1, 2)
w = copy.copy(q)
w.a = 3
print(q.a, q.b)