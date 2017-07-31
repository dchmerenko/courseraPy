str = input()

res = ''

i = 0
lenstr = len(str)
while i < lenstr - 1:
    res += str[i] + '*'
    i += 1

res += str[lenstr - 1]

print(res)
