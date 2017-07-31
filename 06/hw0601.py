# list merging


def merge(a, b):
    c = list()

    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    if i < len(a):
        while i < len(a):
            c.append(a[i])
            i += 1

    if j < len(b):
        while j < len(b):
            c.append(b[j])
            j += 1

    return c


a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(*merge(a, b))
