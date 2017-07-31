def phib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return phib(n - 2) + phib(n - 1)


n = int(input())

print(phib(n))
