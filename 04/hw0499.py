def func():
    x = int(input())
    if x != 0:
        func()
        if int(x ** 0.5) ** 2 == x:
            print(x, end=' ')
            return -1

if func() != -1:
    print(0)
