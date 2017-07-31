# minimal odd

lst = list(map(int, input().split()))

i = 0
while lst[i] % 2 == 0:
    i += 1
minOdd = lst[i]

while i < len(lst):
    if lst[i] % 2 != 0 and lst[i] < minOdd:
        minOdd = lst[i]
    i += 1

print(minOdd)
