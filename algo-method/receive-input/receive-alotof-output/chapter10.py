# 標準出力3-10
N = int(input())
S = [""] * N
for i in range(N):
    S[i] = input()
left = 0
right = 0
for items in S:
    if items == "left":
        left += 1
    else:
        right += 1
if left > right:
    print("left")
elif left < right:
    print("right")
else:
    print("same")
