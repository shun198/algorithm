# データを受け取る
N = int(input())
S = input()

count = 0
# 変数 i の全探索
for i in range(N):
    # 変数 j の全探索
    for j in range(i + 1, N):
        if S[i] == S[j]:
            count += 1

# 答えを出力する
print(count)
