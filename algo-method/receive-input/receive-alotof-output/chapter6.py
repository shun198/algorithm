# 標準出力3-6
N = int(input())
A = list(map(int, input().split()))
total = 0
for items in A:
    total += items
print(total // N)
