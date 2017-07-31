# Petya's place in school line

line = list(map(int, input().split()))
p = int(input())

i = 1

for m in line:
    if p > m:
        break
    i += 1

print(i)
