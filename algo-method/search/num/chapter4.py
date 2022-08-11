# 全探索4
# データを受け取る
A, B = map(int, input().split())

# 線形探索 (1 から min(A,B) まで)
ans = 0
for i in range(1, min(A, B) + 1):
    if A % i == 0 and B % i == 0:
        ans = i
print(ans)
