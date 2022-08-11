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
