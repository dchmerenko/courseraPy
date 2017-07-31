a = int(input())
b = int(input())

if a < b:
    step = 1
else:
    step = -1

for i in range(a, b + step, step):
    print(i, end=' ')
print()
