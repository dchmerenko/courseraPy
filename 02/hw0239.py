x = int(input())

if 0 == x:
    pass
else:
    max1 = x
    x = int(input())
    while x != 0:
        if x == max1:
            max2 = max1
        elif x > max1:
            max2 = max1
            max1 = x
        x = int(input())

print(max2)
