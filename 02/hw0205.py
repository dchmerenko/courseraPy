# -1 1   0 1   1 1
# -1 0     K   1 0
# -1-1   0-1   1-1
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

dx = x2 - x1
dy = y2 - y1

if -1 <= dx <= 1 and -1 <= dy <= 1:
    print("YES")
else:
    print("NO")
