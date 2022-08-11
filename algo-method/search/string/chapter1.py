# 全探索1
S = list(input())
c = input()
flg = False
for i in S:
    if i == c:
        flg = True
        break
if flg:
    print("Yes")
else:
    print("No")
