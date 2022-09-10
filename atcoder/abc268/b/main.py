# コードを記載
S = list(input())
T = list(input())
cnt = 0
flg = True

if len(S) > len(T):
    flg = False
else:
    for i in S:
        if S[cnt] != T[cnt]:
            flg = False
            break
        cnt += 1


if flg == False:
    print("No")
else:
    print("Yes")
