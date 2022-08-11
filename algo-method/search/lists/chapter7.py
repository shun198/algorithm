# 配列の全探索7
N = int(input())
A = list(map(int, input().split()))

index = 0
for i in range(N):
    if A[i] > A[index]:
        index = i
print(index)
