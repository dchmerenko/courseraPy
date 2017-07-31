n = int(input())

m = n % 10

while n // 10 > 0:
    n //= 10
    m = m * 10 + n % 10

print(m)
