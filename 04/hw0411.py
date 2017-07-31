def power(a, n):
    if 0 == n:
        return 1
    else:
        return a * power(a, n - 1)

a = float(input())
n = int(input())

print(power(a, n))
