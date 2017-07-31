# the most frequently word

inf = open('input.txt')
words = inf.read().split()

wordQuantity = {}
for w in words:
    wordQuantity[w] = wordQuantity.get(w, 0) + 1
# print(wordQuantity)

wordFreq = []
for w, q in wordQuantity.items():
    wordFreq += [(q, w)]
wordFreq.sort(key=lambda qw: (-qw[0], qw[1]))
# print(wordFreq)

print(wordFreq[0][1])
inf.close()
