# 標準出力2-1
A, B = map(int, input().split())
print(A+B)

# 標準出力2-2
A, B = map(int, input().split())
if A < B:
    print(B)
elif A > B:
    print(A)
elif A == B:
    print("AとBは大きさが同じです")

# 標準出力2-3
A, B = map(int, input().split())
if A % 10 < B % 10:
    print(A)
else:
    print(B)

# 標準出力2-4
A, B = map(int, input().split())
if A % B == 0:
    print("Yes")
else:
    print("No")

# 標準出力2-5
A, B, C = map(int, input().split())
print(int((A+B+C)/3))

# 標準出力2-6
A, B, C, D = map(int, input().split())
print(max(A, B, C, D))

# 標準出力2-7
S = input()
T = input()
if S == T:
    print("Yes")
else:
    print("No")

# 標準出力2-8
S = input()
T = input()
U = input()
print(U+T+S)

# 標準出力2-9
S = input()
N = int(input())
print(S[N-1])

# 標準出力2-10
S = input()
N, M = map(int, input().split())
S_list = list(S)  # S を配列型に変換する
tmp = S_list[N-1]  # 一時変数に S_list[N-1] を代入する
S_list[N-1] = S_list[M-1]
S_list[M-1] = tmp
S = "".join(S_list)  # 配列の要素を結合して文字列型に変換する
print(S)
