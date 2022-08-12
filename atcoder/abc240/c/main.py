# コードを記載
N, X = map(int, input().split())
Y = [""] * N
A = [0] * N
B = [0] * N
cnt = 0
arr_cnt = 0
for i in range(N):
    Y[i] = input()
for i in Y:
    num_list = list(i)
    A[cnt] = num_list[0]
    B[cnt] = num_list[2]
    cnt += 1
# two_dim_list = [A, B]
# print(two_dim_list)
for i in range(X):
    pass
