myList = list(map(int, input().split()))

positive = 0

for x in myList:
    if x > 0:
        positive += 1

print(positive)
