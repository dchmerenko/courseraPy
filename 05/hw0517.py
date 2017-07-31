myList = list(map(int, input().split()))

prev = myList[0]

for x in myList:
    if x > prev:
        print(x, end=" ")
    prev = x

print()
