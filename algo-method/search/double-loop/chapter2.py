# データを受け取る
N, K = map(int, input().split())

# 数字の全探索
count = 0
for x in range(1, N+1):
    # 約数の個数を求める (数字の全探索)
    yaku = 0
    for i in range(1, x+1):
        if x % i == 0:
            yaku += 1
    # 約数の個数が $K$ 個ならば 1 を足す
    if yaku == K:
        count += 1

# 答えを出力する
print(count)
