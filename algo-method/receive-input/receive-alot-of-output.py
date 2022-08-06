# 標準出力3-1
N = int(input())
A = list(map(int, input().split()))
total = 0
for items in A:
    total += items
print(total)

# 標準出力3-2
N = int(input())
A = list(map(int, input().split()))
total = 1
for items in A:
    total *= items
print(total)

# 標準出力3-3
N = int(input())
A = list(map(int, input().split()))
for items in A:
    print(items % 10)

# 標準出力3-4
N = int(input())
A = list(map(int, input().split()))
for items in A:
    if items % 3 == 0:
        print(items)

# 標準出力3-5
N = int(input())
A = list(map(int, input().split()))
A.reverse()
for items in A:
    print(items)

# 標準出力3-6
N = int(input())
A = list(map(int, input().split()))
total = 0
for items in A:
    total += items
print(total//N)

# 標準出力3-7
N = int(input())
A = list(map(int, input().split()))
print(min(A))

# 標準出力3-8
N = int(input())
A = [""] * N
for i in range(N):
    A[i] = input()
total = 0
for items in A:
    total += len(items)
print(total)

# 標準出力3-9
N = int(input())  # 入力を整数型として受け取る
A = [""] * N
for i in range(N):
    A[i] = input()  # 入力を文字列型配列として受け取る
ans = ""  # 答え
for item in A:  # A の各要素の頭文字をつなげる
    ans += item[0]
print(ans)

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
