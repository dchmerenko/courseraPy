# president election

inf = open('input.txt', 'r', encoding='utf8')
ouf = open('output.txt', 'w', encoding='utf8')

vote = {}
numberOfVotes = 0
for line in inf:
    candidateName = line.strip()
    vote[candidateName] = vote.get(candidateName, 0) + 1
    numberOfVotes += 1
# print(numberOfVotes, vote)

candVoteList = []
for name, v in vote.items():
    candVoteList += [(name, v)]
candVoteList.sort(key=lambda k: (-k[1], k[0]))
# print(candVoteList)

if candVoteList[0][1] * 2 > numberOfVotes:
    print(candVoteList[0][0], file=ouf)
else:
    print('\n'.join((candVoteList[0][0], candVoteList[1][0])), file=ouf)

inf.close()
ouf.close()
