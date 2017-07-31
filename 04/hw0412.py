def power(a, n):
    res = 1
    if n > 0:
        while n > 0:
            res *= a
            n -= 1
        return res
    else:
        while n < 0:
            res /= a
            n += 1
        return res


a = float(input())
n = int(input())

print(power(a, n))
