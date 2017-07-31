# archiving

diskSize, nUsers = tuple(map(int, input().split()))
userVol = list()
sumUserVol = 0

for user in range(nUsers):
    vol = int(input())
    userVol.append(vol)
    sumUserVol += vol

userVol.sort(reverse=True)

i = 0
while i < len(userVol) and sumUserVol > diskSize:
    sumUserVol -= userVol[i]
    i += 1

print(nUsers - i)
