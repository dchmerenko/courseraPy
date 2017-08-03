from sys import stdin
from copy import deepcopy


class Matrix:
    def __init__(self, lst):
        self.m = deepcopy(lst)

    def __str__(self):
        rows = []
        for row in self.m:
            rows.append('\t'.join(map(str, row)))
        return '\n'.join(rows)

    def size(self):
        return len(self.m), len(self.m[0])

    def __add__(self, other):
        new = Matrix(deepcopy(self.m))
        for i in range(self.size()[0]):
            for j in range(self.size()[1]):
                new.m[i][j] += other.m[i][j]
        return new

    def __mul__(self, num):
        new = Matrix(deepcopy(self.m))
        for i in range(self.size()[0]):
            for j in range(self.size()[1]):
                new.m[i][j] *= num
        return new

    __rmul__ = __mul__


exec(stdin.read())

# m = Matrix([[10, 10], [0, 0], [1, 1]])
# print(m.size())

# m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
# m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
# print(m1)
# print(m2)
# print(m1 + m2)

# m = Matrix([[1, 1, 0], [0, 2, 10], [10, 15, 30]])
# alpha = 15
# print(m * alpha)
# print(alpha * m)
