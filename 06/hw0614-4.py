# limit score

inf = open('input.txt', 'r', encoding='utf8')
ouf = open('output.txt', 'w', encoding='utf8')

numSubjects = 3
maxScore = 100
minScore = 40
pupils = [0] * (numSubjects * (maxScore - minScore) + 1)

k = int(inf.readline())

for s in inf:
    line = s.split()
    s1, s2, s3 = int(line[-3]), int(line[-2]), int(line[-1])
    if not (s1 < minScore or s2 < minScore or s3 < minScore):
        pupils[s1 + s2 + s3 - minScore * numSubjects] += 1

numOfPupils = 0
isFirst = True

i = numSubjects * (maxScore - minScore)
while i >= 0:
    pi = pupils[i]
    if pi > 0:
        if isFirst:
            isFirst = False
            if pi > k:
                scoreLimit = 1
                break
        if numOfPupils + pi <= k:
            scoreLimit = i + minScore * numSubjects
        numOfPupils += pi
    i -= 1

if scoreLimit != 1 and numOfPupils <= k:
    scoreLimit = 0

print(scoreLimit, file=ouf)
inf.close()
ouf.close()
