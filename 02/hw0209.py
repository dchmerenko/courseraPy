n = int(input())

# korova 1

# korovy 2 3 4

# korov 0 5 6 7 8 9 10 - 20

ending = ''

if not(9 < n < 21):
    if 1 < n % 10 < 5:
        ending = 'y'
    elif n % 10 == 1:
        ending = 'a'

print(n, 'korov' + ending)
