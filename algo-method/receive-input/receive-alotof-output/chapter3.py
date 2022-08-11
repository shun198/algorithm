# 標準出力3-3
N = int(input())
A = list(map(int, input().split()))
for items in A:
    print(items % 10)
