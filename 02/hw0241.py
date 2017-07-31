n = int(input())

# f0 = 0
# f1 = 1
# fn = fn-1 + fn-2

if 0 == n:
    fi = 0
elif 1 == n:
    fi = 1

i = 1
fi1 = 1
fi2 = 0

while i < n:
    fi = fi1 + fi2
    fi2 = fi1
    fi1 = fi
    i += 1

print(fi)
