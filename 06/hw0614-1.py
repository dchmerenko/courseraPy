# limit score

inf = open('input.txt', 'r', encoding='utf8')
ouf = open('output.txt', 'w', encoding='utf8')

numSubject = 3
maxScore = 100
minScore = 40
pupils = [0] * (numSubject * maxScore + 1)

k = int(inf.readline())

for s in inf:
    line = s.split()
    s1, s2, s3 = int(line[-3]), int(line[-2]), int(line[-1])
    if not (s1 < minScore or s2 < minScore or s3 < minScore):
        pupils[s1 + s2 + s3] += 1
        print(s.strip(), s1 + s2 + s3, pupils[s1 + s2 + s3])

print(pupils)

sumScores = 0
isFirst = True
isChecked = False
scoreLimit = -1
i = numSubject * maxScore
while True:
    print(i, end=' ')
    print(pupils[i])
    i -= 1
    if i < 0:
        break
