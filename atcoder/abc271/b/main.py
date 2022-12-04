# 入力の受け取り
N, Q = map(int, input().split())

# 空のリストを作る
a = []

# てきとうな数列で0番目を埋める
a.append([0])

# N回
for i in range(N):
    # 入力の受け取り
    La = list(map(int, input().split()))
    # aに追加
    a.append(La)

# Q回
for i in range(Q):
    # 入力の受け取り
    s, t = map(int, input().split())
    # s番目のリストのt番目を出力
    print(a[s][t])
