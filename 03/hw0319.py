str = input()

firstpos = str.find('f')
if -1 == firstpos:
    print(-2)
else:
    secondpos = str.find('f', firstpos + 1)
    if -1 == secondpos:
        print(-1)
    else:
        print(secondpos)
