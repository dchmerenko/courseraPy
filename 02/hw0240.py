x = int(input())
max = x
nmax = 0

while x != 0:
    if x > max:
        max = x
        nmax = 1
    elif x == max:
        nmax += 1
    x = int(input())

print(nmax)
