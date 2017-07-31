lst = list(map(int, input().split()))

i = 0
while lst[i] <= 0:
    i += 1

minPositive = lst[i]

for j in range(i + 1, len(lst)):
    if 0 < lst[j] < minPositive:
        minPositive = lst[j]

print(minPositive)
