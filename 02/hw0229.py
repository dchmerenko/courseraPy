n = int(input())

i = 1
while i < n:
    print(i, end=' ')
    i = i * 2
print(i)
if i == n:
    print("YES")
else:
    print("NO")
