# quantity of diffrent numbers

i = open('input.txt', 'r', encoding='utf8')
o = open('output.txt', 'w', encoding='utf8')

a = map(int, i.readline().split())
b = map(int, i.readline().split())

print(*sorted(set(a) & set(b)), file=o)

i.close()
o.close()
