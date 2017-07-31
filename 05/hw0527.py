# remove i-th element

lst = list(map(int, input().split()))
k, c = tuple(map(int, input().split()))

lst.insert(k, c)

print(*lst)
