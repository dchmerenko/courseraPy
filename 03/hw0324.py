str = input()

firstpos = str.find('h')
lastpos = str.rfind('h')

begin = str[:firstpos + 1]
middle = str[firstpos + 1:lastpos].replace('h', 'H')
end = str[lastpos:]

print(begin + middle + end)
