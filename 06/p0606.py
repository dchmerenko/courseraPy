# asylum


def dist(x):
    return x[1]


def num(x):
    return x[0]


n = int(input())
v1 = list(map(int, input().split()))
v = [(i, v1[i]) for i in range(n)]
v.sort(key=dist)

m = int(input())
a1 = list(map(int, input().split()))
a = [(i, a1[i]) for i in range(m)]
a.sort(key=dist)

# print(v, len(v))
# print(a, len(a))

res = []

i = 0
j = 0
while i < len(v):
    mindist, minj = abs(v[i][1] - a[j][1]), j
    while j < len(a):
        va = abs(v[i][1] - a[j][1])
        if va <= mindist:
            mindist, minj = va, j
            # print(v[i], a[j], v[i], a[minj])
            j += 1
        else:
            break
    res.append((v[i][0], a[minj][0]))
    i += 1
    j = minj

res.sort(key=num)

print(*[res[i][1] + 1 for i in range(len(res))])
