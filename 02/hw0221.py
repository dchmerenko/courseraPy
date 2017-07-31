# ax + b / cx + d = 0

# ax + b = 0
# x = -b/a

# 2 * 2 + -4 / 7 * 2 + 1          2
# 1 * -1 + 1 / 2 * -1 + 2 = 0 / 0 NO
# 0 * x + 0                       INF

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a == 0 and b == 0:
    res = "INF"
elif a != 0 and b % a == 0 and (c * -b // a + d) != 0:
    # print("-b // a = {}, c * -b // a + d = {}".format(-b//a,c*-b//a+d))
    res = -b // a
else:
    res = "NO"

print(res)
