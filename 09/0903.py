from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


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
        if self.size() == other.size():
            for i in range(self.size()[0]):
                for j in range(self.size()[1]):
                    new.m[i][j] += other.m[i][j]
        else:
            raise MatrixError(self, other)
        return new

    def __mul__(self, num):
        newm = Matrix(deepcopy(self.m))
        for i in range(self.size()[0]):
            for j in range(self.size()[1]):
                newm.m[i][j] *= num
        return newm

    __rmul__ = __mul__

    def transpose(self):
        # транспонирование квадратной матрицы
        def transform_square(m):
            for i in range(len(m)):
                for j in range(i + 1, len(m[0])):
                    m[j][i], m[i][j] = m[i][j], m[j][i]

        # транспонирование прямоугольной матрицы rows х cols
        rows = self.size()[0]
        cols = self.size()[1]
        # если rows == cols
        if rows == cols:
            transform_square(self.m)
        # если rows > cols
        if rows > cols:
            # добавляем каждой строке rows - cols элементов
            for row in self.m:
                row.extend([0] * (rows - cols))
            # транспонируем прямоугольную матрицу
            transform_square(self.m)
            # удаляем последние rows - cols строк
            for i in range(rows - cols):
                self.m.pop()
        # если rows < cols
        if rows < cols:
            # добавляем в конец строку из rows элементов cols - rows раз
            for i in range(cols - rows):
                self.m.extend([[0] * cols])
            print('rows < cols\nextended m')
            print(m)
            # транспонируем прямоугольную матрицу
            transform_square(self.m)
            # удаляем из всех строк cols - rows последних элементов
            for row in self.m:
                for i in range(cols - rows):
                    row.pop()
        return self

# exec(stdin.read())

# m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
# m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
# print(m1 + m2)
#
# m2 = Matrix([[0, 1, 0], [20, 0, -1]])
# try:
#     m = m1 + m2
#     print('WA\n' + str(m))
# except MatrixError as e:
#     print(e.matrix1)
#     print(e.matrix2)

m = Matrix([[10, 10], [0, 0], [1, 1]])
print(m)
m1 = m.transpose()
print(m)
print(m1)