# sort by counting


def countSort(lst):
    maxLen = 100
    grades = [0] * (maxLen + 1)
    res = []
    for x in lst:
        grades[x] += 1
    for i in range(len(grades)):
        # print((str(i) + ' ') * grades[i], end='')
        res.extend([i] * grades[i])
    lst[:] = res


lst = list(map(int, input().split()))
countSort(lst)

print(*lst)
