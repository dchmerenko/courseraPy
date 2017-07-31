str = input()

firstpos = str.find('h')
lastpos = str.rfind('h')
print(str[:firstpos + 1] + str[firstpos + 1:lastpos] * 2 + str[lastpos:])
