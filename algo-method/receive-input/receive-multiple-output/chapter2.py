# 標準出力2-2
A, B = map(int, input().split())
if A < B:
    print(B)
elif A > B:
    print(A)
elif A == B:
    print("AとBは大きさが同じです")
