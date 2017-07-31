p, x, y, k = int(input()), int(input()), int(input()), int(input())

i = 0
while i < k:
    sum100 = ((x * 100 + y) * (1 + 0.01 * p))
    sumrub = int(sum100 / 100)
    sumkop = int(sum100 + 0.005) - sumrub * 100
    x, y = sumrub, sumkop
    i += 1

print(sumrub, sumkop)
