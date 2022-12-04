# データを受け取る
L, R = map(int, input().split())

# 数字の全探索
count = 0
for x in range(L, R + 1):
    # x が回文数かを調べる
    S = str(x)
    flag = True
    N = len(S)
    for i in range(N):
        if S[i] != S[(N - 1) - i]:
            flag = False
    # x が回文数ならば 1 を足す
    if flag:
        count += 1

# 答えを出力する
print(count)
