# olympiad

n = int(input())
participants = []

for i in range(n):
    name, score = input().split()
    participants.append((name, int(score)))

participants.sort(key=lambda x: x[1], reverse=True)

for p in participants:
    print(p[0])
