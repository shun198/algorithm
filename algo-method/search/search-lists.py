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
for i in range(N-1):
    if A[i] < A[i+1]:
        cnt += 1
print(cnt)

# 配列の全探索6
N = int(input())
A = list(map(int, input().split()))
maxnum = A[0]
for i in range(N):
    if A[i] > maxnum:
        maxnum = A[i]
print(maxnum)

# 配列の全探索7
