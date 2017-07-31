a = int(input())
b = int(input())
c = int(input())

if a > b:
    max = a
else:
    max = b

if c > max:
    max = c

print(max)
