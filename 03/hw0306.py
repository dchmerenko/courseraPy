p, x, y = int(input()), int(input()), int(input())

sum100 = ((x * 100 + y) * (1 + 0.01 * p))
sumrub = int(sum100 / 100)
sumkop = int(sum100 + 0.005) - sumrub * 100

print(sumrub, sumkop)
