# maximum product

lst = list(map(int, input().split()))

if lst[0] > lst[1]:
    max1, max2 = lst[0], lst[1]
    min1, min2 = lst[1], lst[0]
else:
    max1, max2 = lst[1], lst[0]
    min1, min2 = lst[0], lst[1]

i = 2
while i < len(lst):
    x = lst[i]
    i += 1

    if x > max1:
        max2 = max1
        max1 = x
    elif x == max1:
        max2 = x

    if x < min1:
        min2 = min1
        min1 = x
    elif x == min1:
        min2 = x

if min1 * min2 > max1 * max2:
    print(min1, min2)
else:
    print(max2, max1)
