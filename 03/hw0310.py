# sigma = sqrt(((x1 - s) ** 2 + (x2 - s) ** 2 + ... + (xn - s) ** 2) / (n - 1))
# s = (x1 + x2 + ... + xn) / n

sigma = s = store = n = 0

x = int(input())

while x != 0:
    store = 10 * store + x
    s += x
    n += 1
    x = int(input())

s = s / n

while store > 0:
    sigma += (store % 10 - s) ** 2
    store //= 10

sigma = (sigma / (n - 1)) ** 0.5

print(sigma)
