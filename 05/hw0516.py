myList = list(map(int, input().split()))

max = myList[0]
indMax = 0

for i in range(1, len(myList)):
    if myList[i] >= max:
        max = myList[i]
        indMax = i

print(max, indMax)
