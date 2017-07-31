myList = list(map(int, input().split()))

print(*[x for x in myList if x % 2 == 0])
