# 全探索1
N = int(input())
count = 0
for i in range(1, N + 1):
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
        count += 1
print(count)

# 全探索2
N = int(input())
count = 0
for i in range(1, N + 1):
    if N % i == 0:
        count += 1
print(count)

# 全探索3
N = int(input())
flg = True
if N == 1:
    flg = False
for i in range(2, N):
    if N % i == 0:
        flg = False
        break
if flg:
    print("Yes")
else:
    print("No")

# 全探索4
# データを受け取る
A, B = map(int, input().split())

# 線形探索 (1 から min(A,B) まで)
ans = 0
for i in range(1, min(A, B) + 1):
    if A % i == 0 and B % i == 0:
        ans = i

# 全探索5
N = int(input())
for i in range(1, N + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0 and i % 5 != 0:
        print("Fizz")
    elif i % 5 == 0 and i % 3 != 0:
        print("Buzz")
    else:
        print(i)
