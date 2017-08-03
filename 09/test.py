matrix1 = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
# print(*zip(*matrix1))

# транспонирование квадратной матрицы
def transform_square(m):
    for i in range(len(m)):
        for j in range(i + 1, len(m[0])):
            m[j][i], m[i][j] = m[i][j], m[j][i]

# транспонирование прямоугольной матрицы rows х cols

m = matrix1[:1]
print('initial matrix')
print(m)

rows = len(m)
cols = len(m[0])

# если rows == cols
if rows == cols:
    transform_square(m)
    print('rows == cols')
    print(m)

# если rows > cols
#
# 1 2 3
# 4 5 6
# 7 8 9
# 10 11 12
#
if rows > cols:
    # добавляем каждой строке rows - cols элементов
    for row in m:
        row.extend([0] * (rows - cols))
    print('rows > cols\nextended m')
    # транспонируем прямоугольную матрицу
    transform_square(m)
    # удаляем последние rows - cols строк
    for i in range(rows - cols):
        m.pop()
    print(m)

# если rows < cols
#
# 1 2 3
# 4 5 6
#
if rows < cols:
    # добавляем в конец строку из rows элементов cols - rows раз
    for i in range(cols - rows):
        m.extend([[0] * cols])
    print('rows < cols\nextended m')
    print(m)
    # транспонируем прямоугольную матрицу
    transform_square(m)
    # удаляем из всех строк cols - rows последних элементов
    for row in m:
        for i in range(cols - rows):
            row.pop()
    print(m)

# print('changed initial matrix element m[0][1]')
# matrix1[1][3] = 'ch'
# print(m)
# print(matrix1)
