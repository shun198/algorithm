# データを受け取る
N = int(input())
A = list(map(int, input().split()))

# 配列の全探索
counter = 0
for x in A:
    # 素数判定 (数字の全探索)
    is_prime = True
    if x == 1:
        is_prime = False
    else:
        for i in range(2, x):
            if x % i == 0:
                is_prime = False
    # 素数ならば 1 を足す
    if is_prime:
        counter += 1

# 答えを出力する
print(counter)
