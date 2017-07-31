# count different elements

lst = list(map(int, input().split()))
n = 1

i = 1
while i < len(lst):
    if lst[i - 1] != lst[i]:
        n += 1
    i += 1

print(n)
