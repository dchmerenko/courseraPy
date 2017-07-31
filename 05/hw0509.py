a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

nroots = 0

for x in range(1000 + 1):
    if a * x ** 3 + b * x ** 2 + c * x + d == 0:
        if x != e:
            nroots += 1

print(nroots)
