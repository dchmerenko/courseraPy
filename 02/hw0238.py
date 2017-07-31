n = 0
x = int(input())
prev = x

while x != 0:
    if x > prev:
        n += 1
    prev = x
    x = int(input())

print(n)
