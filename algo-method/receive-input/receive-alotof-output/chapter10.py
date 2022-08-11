# 標準出力3-10
N = int(input())
A = [""] * N
left_cnt = 0
right_cnt = 0
for i in range(N):
    A[i] = input()
    if A[i] == "left":
        left_cnt += 1
    elif A[i] == "right":
        right_cnt += 1
if left_cnt > right_cnt:
    print("left")
elif left_cnt < right_cnt:
    print("right")
else:
    print("same")
