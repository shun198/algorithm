# 配列の全探索5
N = int(input())
A = list(map(int, input().split()))
cnt = 0
for i in range(N - 1):
    if A[i] < A[i + 1]:
        cnt += 1
print(cnt)
