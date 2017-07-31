str = input()

firstpos = str.find('h')
lastpos = str.rfind('h')
print(str[:firstpos] + str[lastpos + 1:])
