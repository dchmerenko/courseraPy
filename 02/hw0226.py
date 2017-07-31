n = int(input())

if n < 2:
    print(1)
else:
    i = 2
    while n % i != 0:
        i += 1
    print(i)
