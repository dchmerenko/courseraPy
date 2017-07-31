lst = list(map(int, input().split()))

imax = 0
max = lst[imax]

for i in range(1, len(lst)):
    if lst[i] > max:
        max = lst[i]
        imax = i

print(max, imax)
