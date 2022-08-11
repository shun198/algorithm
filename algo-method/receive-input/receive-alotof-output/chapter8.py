# 標準出力3-8
N = int(input())
A = [""] * N
for i in range(N):
    A[i] = input()
total = 0
for items in A:
    total += len(items)
print(total)

# # 別解
# N = int(input())
# # N個分の要素を入れることができる空のlistを用意
# S = [""] * N
# # N個分代入していく
# for i in range(N):
#     S[i] = input()
# print(len("".join(S)))
