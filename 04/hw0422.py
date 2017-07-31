def lagrange(n):
    sqrn = int(n ** 0.5)
    for a in range(sqrn + 1):
        for b in range(sqrn + 1):
            for c in range(sqrn + 1):
                for d in range(sqrn + 1):
                    # print("a = {} b = {} c = {} d = {}".format(a, b, c, d))
                    if a * a + b * b + c * c + d * d == n:
                        return a, b, c, d


n = int(input())

for i in lagrange(n):
    if 0 != i:
        print(i, end=' ')

print()
