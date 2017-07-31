# Notebooks in the Store

a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())

res = 0

# sorting notebook sizes
if a2 > b2:
    a2, b2 = b2, a2
if b2 > c2:
    b2, c2 = c2, b2
if a2 > b2:
    a2, b2 = b2, a2

# case 1. a - a, b - b, c - c.
na = a1 // a2
nb = b1 // b2
nc = c1 // c2
n = na * nb * nc
if n > res:
    res = n

# case 2. a - a, b - c, c - b.
na = a1 // a2
nb = b1 // c2
nc = c1 // b2
n = na * nb * nc
if n > res:
    res = n

# case 3. a - b, b - a, c - c
na = a1 // b2
nb = b1 // a2
nc = c1 // c2
n = na * nb * nc
if n > res:
    res = n

# case 4. a - b, b - c, c - a
na = a1 // b2
nb = b1 // c2
nc = c1 // a2
n = na * nb * nc
if n > res:
    res = n

# case 5. a - c, b - a, c - b
na = a1 // c2
nb = b1 // a2
nc = c1 // b2
n = na * nb * nc
if n > res:
    res = n

# case 6. a - c, b - b, c - a
na = a1 // c2
nb = b1 // b2
nc = c1 // a2
n = na * nb * nc
if n > res:
    res = n

print(res)
