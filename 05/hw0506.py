n = int(input())
nzero = 0

for i in range(n):
    x = int(input())
    if x == 0:
        nzero += 1

print(nzero)
