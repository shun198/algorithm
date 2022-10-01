# コードを記載
N,Q = map(int, input().split())
L = [""] * N
# 数字なら A = [0] * N
# N個分代入していく
for i in range(N):
    L[i] = input()
