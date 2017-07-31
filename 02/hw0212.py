x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

dy = y2 - y1
dx = x2 - x1
if dx < 0:
    dx = -dx

if (dx <= dy) and ((x1 + y1) % 2 == (x2 + y2) % 2):
    print("YES")
else:
    print("NO")
