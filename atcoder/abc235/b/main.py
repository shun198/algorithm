# コードを記載
N = int(input())
H = list(map(int, input().split()))
num = H[0]
for i in range(N - 1):
    if H[i] < H[i + 1]:
        num = H[i + 1]
    else:
        break
print(num)
