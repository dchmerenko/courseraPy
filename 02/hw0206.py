first = int(input())
last = int(input())

initial = 1

if (first - 1) % (last - first + 1) == 0:
    print("YES")
else:
    print("NO")
