# 標準出力2-3
A, B = map(int, input().split())
if A % 10 < B % 10:
    print(A)
else:
    print(B)
