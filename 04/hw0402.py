def dist(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())

p = dist(x1, y1, x2, y2) + dist(x2, y2, x3, y3) + dist(x3, y3, x1, y1)

print(p)
