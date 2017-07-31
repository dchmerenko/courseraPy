# sorted pupil

fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')

lines = fin.readlines()
lines.sort()

for line in lines:
    ls = line.split()
    print(' '.join([ls[0], ls[1], ls[3]]))
