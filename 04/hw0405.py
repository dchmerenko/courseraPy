def ifPointInSquare(x, y):
    return abs(x) + abs(y) <= 1

x = float(input())
y = float(input())

if ifPointInSquare(x, y):
    print("Yes")
else:
    print("No")
