# コードを記載
N,M = map(int, input().split())
cnt_list = [0]*N
flg = True
for i in range(M):
    party_list = list(map(int, input().strip().split()))
    party_set = set(party_list[1:])
    for j in party_set:
        if cnt_list[j- 1] <= 2:
            cnt_list[j-1] += 1
for k in set(cnt_list):
    if k == 0 or k ==1:
        flg = False
        break
if flg:
    print("Yes")
else:
    print("No")
