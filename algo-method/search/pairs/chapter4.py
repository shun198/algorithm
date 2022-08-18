# データを受け取る
N = int(input())
S = [input().split() for _ in range(N)]

flag = False
# 変数 i の全探索
for i in range(N):
    # 変数 j の全探索
    for j in range(i + 1, N):
        if S[i] == S[j]:
            flag = True

# 答えを出力する
if flag:
    print("Yes")
else:
    print("No")
