# 配列の全探索1
N, V = map(int, input().split())
A = list(map(int, input().split()))
flg = False
for items in A:
    if items == V:
        flg = True
        break
if flg:
    print("Yes")
else:
    print("No")

# 配列の全探索2
N, V = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
for items in A:
    if items == V:
        cnt += 1
print(cnt)

# 配列の全探索3
N = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
for items in A:
    if items > 0:
        cnt += 1
print(cnt)

# 配列の全探索4
N, V = map(int, input().split())
A = list(map(int, input().split()))
cnt_to_right = -1
for i in range(N):
    if A[i] == V:
        cnt_to_right = i
print(cnt_to_right)

# 配列の全探索5
N = int(input())
A = list(map(int, input().split()))
cnt = 0
for i in range(N - 1):
    if A[i] < A[i + 1]:
        cnt += 1
print(cnt)

# 配列の全探索6
N = int(input())
A = list(map(int, input().split()))
max = A[0]
for i in range(N):
    if A[i] > max:
        max = A[i]
print(max)

# 配列の全探索7
N = int(input())
A = list(map(int, input().split()))

index = 0
for i in range(N):
    if A[i] > A[index]:
        index = i
print(index)

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

# 配列の全探索9
# データを受け取る
N = int(input())
A = list(map(int, input().split()))

# 線形探索
count = [0] * 9
for x in A:
    count[x - 1] += 1

# 答えを出力する
for x in count:
    print(x)


# 配列の全探索10
# データを受け取る
N = int(input())
A = list(map(int, input().split()))

# 線形探索 (集計)
count = [0] * 9
for x in A:
    count[x - 1] += 1

# 線形探索 (最大値)
index = 0
for i in range(9):
    if count[i] > count[index]:
        index = i

# 答えを出力する
ans = index + 1
print(ans)
