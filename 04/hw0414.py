def power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power(a * a, n // 2)
    elif n % 2 != 0:
        if n > 0:
            return a * power(a, n - 1)
        else:
            return 1 / a * power(a, n + 1)


a = float(input())
n = int(input())

print(power(a, n))
