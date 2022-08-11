# 配列の全探索2
N, V = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
for items in A:
    if items == V:
        cnt += 1
print(cnt)
