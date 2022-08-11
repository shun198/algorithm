# 標準出力2-10
S = list(input())
N, M = map(int, input().split())
S_temp = S[N-1]
S[N-1] = S[M-1]
S[M-1] = S_temp
S = "".join(S)
print(S)
