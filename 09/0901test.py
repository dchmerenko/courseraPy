# class Matrix
from sys import stdin
from copy import deepcopy


class Matrix:
    def __init__(self, *args):
        for arg in deepcopy(args):
            self.row = arg[:]

    def __str__(self):
        return '\n'.join(map(lambda x: '\t'.join(map(str, x)), self.row))

    def __add__(self, other):
        newMatrix = deepcopy(self)
        for i in range(newMatrix.size()[0]):
            for j in range(newMatrix.size()[1]):
                newMatrix[i][j] += other[i][j]
        return newMatrix

    def size(self):
        return len(self.row), len(self.row[0])

#exec(stdin.read())

# r1 = [1, 0]
# r2 = [0, 1]
# m1 = Matrix([r1, r2])
# m2 = Matrix([r1, r2])
# print(m1)
# print(m2)
# r1[0] = 1234567890
# print(m1)
# print(m2)

m = Matrix([[1, 1, 1], [0, 100, 10]])
print(str(m) == '1\t1\t1\n0\t100\t10')