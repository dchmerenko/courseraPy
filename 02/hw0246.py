x = int(input())
prev = x - 1

n = 1
nmax = 1

while x != 0:
    if x == prev:
        n += 1
        if n > nmax:
            nmax = n
    else:
        n = 1
        prev = x
    x = int(input())

print(nmax)
