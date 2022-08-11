# 配列の全探索3
N = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
for items in A:
    if items > 0:
        cnt += 1
print(cnt)
