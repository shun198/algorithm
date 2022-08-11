# 標準出力3-5
N = int(input())
A = list(map(int, input().split()))
A.reverse()
for items in A:
    print(items)

# 別解
# N = int(input())
# A = list(map(int, input().split()))
# for i in range(N):
#     print(A[N-i-1])
