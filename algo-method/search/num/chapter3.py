# 全探索3
N = int(input())
flg = True
if N == 1:
    flg = False
for i in range(2, N):
    if N % i == 0:
        flg = False
        break
if flg:
    print("Yes")
else:
    print("No")
