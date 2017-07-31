st = input()

i = 0
while i < len(st):
    if i % 3 != 0:
        print(st[i], end='')
    i += 1

print()
