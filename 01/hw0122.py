a = int(input())
b = int(input())

t1 = a // b
t2 = (t1 + 2) % (t1 + 1)
t3 = t2 % 2

print(t1, t2, t3)
