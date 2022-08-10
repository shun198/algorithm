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

# 全探索4
N = int(input())
S = input()
T = input()
count = 0
for i in range(N):
    if S[i] != T[i]:
        count += 1
print(count)
