# コードを記載
N, M = map(int, input().split())
S = list(map(str, input().split()))
T = set(map(str, input().split()))
for items in S:
    if items in T:
        print("Yes")
    else:
        print("No")
