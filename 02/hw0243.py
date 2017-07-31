a, b = int(input()), int(input())

while a != b:
    if a < 2 * b:
        print("-1")
        a -= 1
    else:
        if a % 2 != 0:
            print("-1")
            a -= 1
        else:
            print(":2")
            a //= 2
