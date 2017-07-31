a = str(7337)
b = str(7447)

start = int(a[0] + a[1])
end = int(b[0] + b[1])

i = start
res = int(a)

while res <= int(b):
    s = str(i)
    res = int(s[0] + s[1] + s[1] + s[0])
    print(res)
    i += 1
