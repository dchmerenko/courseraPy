n = int(input())

sum = (n + 1) * n // 2

for i in range(n - 1):
    sum -= int(input())

print(sum)
