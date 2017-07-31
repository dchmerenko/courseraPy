def rev():
    n = int(input())
    if n != 0:
        rev()
    print(n)


rev()
