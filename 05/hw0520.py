lst = list(map(int, input().split()))

q = 0

for i in range(2, len(lst)):
    isMax = lst[i - 2] < lst[i - 1] > lst[i]
    if isMax:
        q += 1

print(q)
