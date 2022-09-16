# コードを記載
# import numpy as np

# H, W = map(int, input().split())
# A = [0] * H
# # N個分代入していく
# for i in range(H):
#     A[i] = input().split()
# reverse_num_list = np.array(A)
# tr = reverse_num_list.T
# for j in tr:
#     print(*j)

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
A = list(zip(*A))
for i in A:
    print(*i)

L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(L)
print(list(zip(*L)))
