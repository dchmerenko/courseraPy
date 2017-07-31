a = int(input())
b = int(input())
c = int(input())

if a > b:
    temp = a
    a = b
    b = temp

if b > c:
    temp = b
    b = c
    c = temp

result = c ** 2 - b ** 2 - a ** 2

if result < 0:
    print("acute")
elif result == 0:
    print("rectangular")
elif result > 0 and c < a + b:
    print("obtuse")
else:
    print("impossible")
