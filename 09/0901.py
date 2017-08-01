# class Matrix


class Matrix:
    def __init__(self, *args):
        for arg in args:
            self.row = arg[:]
    # def __str__(self):
    #     sMatrix = list()
    #     for r in self.row:
    #         sRow = '\t'.join(map(str, r))
    #         sMatrix.append(sRow)
    #     return '\n'.join(sMatrix)

    def __str__(self):
        return '\n'.join(map(lambda x: '\t'.join(map(str, x)), self.row))

    def size(self):
        return len(self.row), len(self.row[0])

m = Matrix([[1, 0], [0, 1]])

print(m.row[0])
print(m.row[1])
print(m.size())
print(m)