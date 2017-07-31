# avarage score

fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')

sum9, num9 = 0, 0
sum10, num10 = 0, 0
sum11, num11 = 0, 0

for line in fin:
    clss, mark = int(line.split()[2]), int(line.split()[3])

    if clss == 9:
        num9 += 1
        sum9 += mark
    elif clss == 10:
        num10 += 1
        sum10 += mark
    elif clss == 11:
        num11 += 1
        sum11 += mark

print(sum9 / num9, sum10 / num10, sum11 / num11)
