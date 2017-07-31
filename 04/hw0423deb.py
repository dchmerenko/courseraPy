def cubes(n):
    root3 = int(n ** (1 / 3))
    for x1 in range(root3 + 1):
        for x2 in range(root3 + 1):
            for x3 in range(root3 + 1):
                for x4 in range(root3 + 1):
                    for x5 in range(root3 + 1):
                        for x6 in range(root3 + 1):
                            for x7 in range(root3 + 1):
                                sumcubes = x1 ** 3 + x2 ** 3 + x3 ** 3 + x4 ** 3 + x5 ** 3 + x6 ** 3 + x7 ** 3
                                print("x1 = {} x2 = {} x3 = {} x4 = {} x5 = {} x6 = {} x7 = {} sum = {}".format(x1, x2, x3, x4, x5, x6, x7, sumcubes))
                                if sumcubes == n:
                                    return x1, x2, x3, x4, x5, x6, x7
                                if sumcubes > n:
                                    break
    return 0, 0, 0, 0, 0, 0, 0

n = int(input())

sum = 0
res = cubes(n)

print("res =", res)

for x in res:
    sum += x
    if x != 0:
        print(x ** 3, end=' ')
print()
        
if 0 == sum:
    print(0)
