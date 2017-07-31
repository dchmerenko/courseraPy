# YES or NO if number was earlier

seq = map(int, input().split())
seqSet = set()
for s in seq:
    if s in seqSet:
        print("YES")
    else:
        seqSet.add(s)
        print("NO")
