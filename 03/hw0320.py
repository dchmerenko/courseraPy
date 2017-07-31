str = input()

sp = str.find(' ')
res = str[sp + 1:] + str[sp] + str[:sp]

print(res)
