x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x1 > 0:
    if y1 > 0:
        sector1 = 1
    else:
        sector1 = 4
else:
    if y1 > 0:
        sector1 = 2
    else:
        sector1 = 3

if x2 > 0:
    if y2 > 0:
        sector2 = 1
    else:
        sector2 = 4
else:
    if y2 > 0:
        sector2 = 2
    else:
        sector2 = 3

if sector1 == sector2:
    print("YES")
else:
    print("NO")
