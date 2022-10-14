# コードを記載
N = int(input())
A = list(map(int, input().strip().split()))
flg = True
sort_even = sorted(A,reverse=True)
for i in range(1,N):
    if (sort_even[0] + sort_even[i]) % 2 == 0:
        print(sort_even[0] + sort_even[i])
        flg = False
        break
if flg:
    print(-1)
