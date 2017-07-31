def isAscending(myList):
    i = 1
    while i < len(myList) and myList[i - 1] < myList[i]:
        i += 1
    return "YES" if i == len(myList) else "NO"


myList = list(map(int, input().split()))

print(isAscending(myList))
