x = int(input())
y = int(input())

xx = x
d = 1

while xx < y:
    xx += xx / 10
    d += 1

print(d)
