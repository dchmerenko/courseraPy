# cubes

na, mb = tuple(map(int, input().split()))
a = set()
b = set()
for i in range(na):
    a.add(int(input()))
for i in range(mb):
    b.add(int(input()))

intersectionAB = a & b
print(len(intersectionAB))
print(*sorted(intersectionAB))

differenceAB = a - b
print(len(differenceAB))
print(*sorted(differenceAB))

differenceBA = b - a
print(len(differenceBA))
print(*sorted(differenceBA))
