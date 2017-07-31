h = int(input())
a = int(input())
b = int(input())

h0 = h - a
h1 = a - b

n = 1 + h0 // h1 + (h0 % h1 + h1 - 1) // h1

print(n)
