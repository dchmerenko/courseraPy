a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())

x = (d * e - f * b) / (a * d - b * c)
y = (a * f - c * e) / (a * d - b * c)

print(x, y)
