x = int(input())

# f0 = 0
# f1 = 1
# fn = fn-1 + fn-2
# n  0 1 2 3 4 5 6  7  8  9 10 11  12
# fn 0 1 1 2 3 5 8 13 21 34 55 89 144

if 0 == x:
    n = 0
elif 1 == x:
    n = "1 or 2"
else:
    n = 1
    fi = 1
    fi1 = 1
    fi2 = 0
    while fi < x:
        fi = fi1 + fi2
        fi2 = fi1
        fi1 = fi
        n += 1
    if fi != x:
        n = -1

print(n)
