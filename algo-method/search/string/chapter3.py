# 全探索3
# データを受け取る
S = input()

# S の長さを取得する
N = len(S)

# 線形探索 (0 から N-2 まで)
count = 0
for i in range(N - 1):
    if S[i] == S[i + 1]:
        count += 1
print(count)
