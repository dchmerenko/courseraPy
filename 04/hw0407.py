def ifPointInArea(x, y):
    inArea1 = y >= -x and y >= 2 * x + 2 and (x + 1) ** 2 + (y - 1) ** 2 <= 4
    inArea2 = y <= -x and y <= 2 * x + 2 and (x + 1) ** 2 + (y - 1) ** 2 >= 4
    return inArea1 or inArea2


x = float(input())
y = float(input())

if ifPointInArea(x, y):
    print("Yes")
else:
    print("No")
