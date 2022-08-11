# 標準出力3-2
N = int(input())
A = list(map(int, input().split()))
total = 1
for items in A:
    total *= items
print(total)
