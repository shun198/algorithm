# 全探索1
S = list(input())
c = input()
flg = False
for i in S:
    if i == c:
        flg = True
        break
if flg:
    print("Yes")
else:
    print("No")

# 全探索2
# データを受け取る
S = input()

# S の長さを取得する
N = len(S)

# 線形探索
flag = True
for i in range(N):
    if S[i] != S[(N - 1) - i]:
        flag = False

# 答えを出力する
if flag:
    print("Yes")
else:
    print("No")