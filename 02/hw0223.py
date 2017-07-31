l1 = int(input())
r1 = int(input())
l2 = int(input())
r2 = int(input())
l3 = int(input())
r3 = int(input())

len1 = r1 - l1
len2 = r2 - l2
len3 = r3 - l3

cross12 = l2 <= r1 <= r2 or l2 <= l1 <= r2
cross13 = l3 <= r1 <= r3 or l3 <= l1 <= r3
cross23 = l3 <= r2 <= r3 or l3 <= l2 <= r3

if cross12:
    dist12 = 0
else:
    if l2 > r1:
        dist12 = l2 - r1
    else:
        dist12 = l1 - r2

if cross13:
    dist13 = 0
else:
    if l3 > r1:
        dist13 = l3 - r1
    else:
        dist13 = l1 - r3

if cross23:
    dist23 = 0
else:
    if l3 > r2:
        dist23 = l3 - r2
    else:
        dist23 = l2 - r3

if cross12 and cross23 or cross12 and cross13 or cross13 and cross23:
    m = 0
elif dist23 <= len1:
    m = 1
elif dist13 <= len2:
    m = 2
elif dist12 <= len3:
    m = 3
else:
    m = -1

# print("m = {} l1 = {} l2 = {} l3 = {}".format(m, len1, len2, len3))
# print("c12 = {} c23 = {} c13 = {}".format(cross12, cross23, cross13))
# print("d12 = {} d23 = {} d13 = {}".format(dist12, dist23, dist13))

print(m)
