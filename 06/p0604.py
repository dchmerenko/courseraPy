# shoes shop

footsize = int(input())
shopstock = list(map(int, input().split()))

shopstock.sort()

n = 0
for shoes in shopstock:
    if shoes < footsize:
        continue
    else:
        n += 1
        footsize = shoes + 3

print(n)
