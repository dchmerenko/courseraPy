myList = list(map(int, input().split()))

max = myList[0]
indMax = 0

for x in myList:
    if x >= max:
        max = x
        indMax = myList.index(x, indMax)

print(max, indMax)
