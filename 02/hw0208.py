n = int(input())
m = int(input())
k = int(input())

cond1 = (k >= n and k % n == 0)
cond2 = (k >= m and k % m == 0)

if (k == 0 or cond1 or cond2) and k <= m * n:
    print("YES")
else:
    print("NO")
