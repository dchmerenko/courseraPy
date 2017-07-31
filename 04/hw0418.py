def c(n, k):
    if 0 <= k <= n:
        if n == 0 and k == 0:
            return 1
        elif n == 1 and k == 0:
            return 1
        elif n == 1 and k == 1:
            return 1
        else:
            return c(n - 1, k) + c(n - 1, k - 1)
    else:
        return 0


n = int(input())
k = int(input())

print(c(n, k))
