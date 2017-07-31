def ifPointInCircle(x, y, xc, yc, r):
    return (x - xc) ** 2 + (y - yc) ** 2 <= r ** 2

x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())

if ifPointInCircle(x, y, xc, yc, r):
    print("Yes")
else:
    print("No")
