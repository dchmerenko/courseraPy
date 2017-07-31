# ax2 + bx +c =0
# d = b2 - 4ac
# x1, x2 = (-b +- d ** 0.5) / 2a

a, b, c = float(input()), float(input()), float(input())

epsilon = 1.0e-7
d = b * b - 4 * a * c

if d > 0:
    x1 = (-b - d ** 0.5) / (2 * a)
    x2 = (-b + d ** 0.5) / (2 * a)
    if x1 > x2:
        x1, x2 = x2, x1
    print(x1, x2)
elif abs(d) < epsilon:
    x = -b / (2 * a)
    print(x)
