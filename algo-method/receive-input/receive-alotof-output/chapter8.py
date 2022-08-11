# 標準出力3-8
N = int(input())
A = [""] * N
for i in range(N):
    A[i] = input()
total = 0
for items in A:
    total += len(items)
print(total)
