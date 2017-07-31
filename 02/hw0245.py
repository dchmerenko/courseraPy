k = input()

p = 0

i = 1
while i <= int(k):
    if str(i) == str(i)[::-1]:
        p += 1
    i += 1

print(p)
