# 標準出力3-4
N = int(input())
A = list(map(int, input().split()))
for items in A:
    if items % 3 == 0:
        print(items)
