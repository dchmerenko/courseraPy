def xor(x, y):
    return 0 < x + y <= 1


x = int(input())
y = int(input())

if xor(x, y):
    print(1)
else:
    print(0)
