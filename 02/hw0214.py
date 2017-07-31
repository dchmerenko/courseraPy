a = int(input())
b = int(input())
c = int(input())

haveEven = a % 2 == 0 or b % 2 == 0 or c % 2 == 0
haveOdd = a % 2 != 0 or b % 2 != 0 or c % 2 != 0

if haveEven and haveOdd:
    print("YES")
else:
    print("NO")
