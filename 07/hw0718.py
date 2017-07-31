# words frequenсy analysis

inf = open('input.txt')
words = inf.read().split()
# print(words)

wordFreq = {}
for w in words:
    wordFreq[w] = wordFreq.get(w, 0) + 1
# print(wordFreq)

wordList = []
for w, q in wordFreq.items():
    wordList += [(q, w)]
wordList.sort(key=lambda qw: (-qw[0], qw[1]))
# print(wordList)

print('\n'.join([str(qw[1]) for qw in wordList]))
inf.close()
