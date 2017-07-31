x2, x1 = int(input()), int(input())

n = 1
nmax = 1

# если x[i-1] и x[i] не равны и знак роста не менялся, то счетчик n++ и если n>max то max = n
# иначе сбрасываем счетчик n = 1  

while x != 0:
    if x - x1 > 0 and x1 - x2 > 0 or x - x1 < 0 and x1 - x2 < 0:
        n += 1
        if n > nmax:
            nmax = n
    else:
        n = 1
    x2 = x1
    x1 = x
    x = int(input())
    
print(nmax)
