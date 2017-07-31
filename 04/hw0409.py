def minDivisor(n):
    i = 2
    imax = n ** 0.5
    while i <= imax:
        if n % i == 0:
            return i
        i += 1
    return n


n = int(input())

print(minDivisor(n))
