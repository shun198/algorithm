# 配列の全探索4
N, V = map(int, input().split())
A = list(map(int, input().split()))
cnt_to_right = -1
for i in range(N):
    if A[i] == V:
        cnt_to_right = i
print(cnt_to_right)
