# 配列の全探索8
# データを受け取る
N = int(input())
A = list(map(int, input().split()))

# 線形探索
min = A[0]
for x in A:
    if x < min:
        min = x

# 答えを出力する
print(min)
