str = input()

firstpos = str.find('f')
lastpos = str.rfind('f')
if firstpos != -1:
    print(firstpos)
    if lastpos > firstpos:
        print(lastpos)
