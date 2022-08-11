# データを受け取る
N = int(input())
S = [input() for _ in range(N)]

# 配列の全探索
count = 0
for x in S:
    # x が回文かを調べる
    flag = True
    N = len(x)
    for i in range(N):
        if x[i] != x[(N - 1) - i]:
            flag = False
    # x が回文ならば 1 を足す
    if flag:
        count += 1

# 答えを出力する
print(count)
