arg = [[1, 0], [0, 1]]

a0 = map(str, arg[0])
#print(*a0)


def make_str_t(lst):
    return '\t'.join(map(str, lst))

print('\n'.join(map(lambda x: '\t'.join(map(str, x)), arg[:])))