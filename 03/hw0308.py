# p = an * x ** n + an-1 * x ** n-1 + ... + a1 * x + a0

n, x = int(input()), float(input())

p = 0
i = 0
while i < n:
    a = float(input())
    p = (p + a) * x
    i += 1
p += float(input())

print(p)
