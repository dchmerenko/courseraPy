def gcd(a, b):
    if 0 == b:
        return a
    else:
        return gcd(b, a % b)

a = int(input())
b = int(input())

print(gcd(a, b))
