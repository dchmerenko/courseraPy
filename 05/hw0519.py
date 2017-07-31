lst = list(map(int, input().split()))

for i in range(1, len(lst)):
    neg = lst[i - 1] < 0 and lst[i] < 0
    pos = lst[i - 1] > 0 and lst[i] > 0
    if pos or neg:
        print(lst[i - 1], lst[i])
        break
