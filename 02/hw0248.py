x2 = x1 = x = int(input())

nmax = n = 0

if 0 == x:
    n = 0
    nmax = 0
else:
    while x != 0:
        if x == x1:
            n = 1
            if nmax < n:
                nmax = n
        if (x != x1 and x1 == x2) or x > x1 and x1 < x2 or x < x1 and x1 > x2:
            n = 2
            if nmax < n:
                nmax = n
        if (x > x1 and x1 > x2) or (x < x1 and x1 < x2):
            n += 1
            if nmax < n:
                nmax = n
        x2 = x1
        x1 = x
        x = int(input())

print(nmax)
