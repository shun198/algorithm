# データを受け取る
L, R = map(int, input().split())

count = 0
# 変数 i の全探索
for i in range(L, R + 1):
    # 変数 j の全探索
    for j in range(i + 1, R + 1):
        if i % 10 == j % 10:
            count += 1

# 答えを出力する
print(count)
