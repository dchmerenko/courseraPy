lst = list(map(int, input().split()))

imin = imax = 0

for i in range(len(lst)):
    if lst[i] < lst[imin]:
        imin = i
    if lst[i] > lst[imax]:
        imax = i

lst[imin], lst[imax] = lst[imax], lst[imin]

print(*lst)
