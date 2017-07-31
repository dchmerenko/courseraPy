def gcd(a, b):
    if 0 == b:
        return a
    else:
        return gcd(b, a % b)

n = int(input())
m = int(input())

d = gcd(n, m)

print(n // d, m // d)
