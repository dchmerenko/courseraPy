n = int(input())

f1 = "+___ "
f2 = "|* / "
f3 = "|__\ "
f4 = "|    "

print(f1 * n)
for i in range(n):
    print(f2[:1] + str(i + 1) + f2[2:], end='')
print()
print(f3 * n)
print(f4 * n)
