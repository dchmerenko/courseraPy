n = int(input())

sum = 0
fct = 1

for i in range(1, n + 1):
    fct *= i
    sum += fct

print(sum)
