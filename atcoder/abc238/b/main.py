# コードを記載
N = int(input())
A = list(map(int, input().split()))
pizza_deg = [0] * (N + 1)
deg_diff = [0] * (N + 1)
deg = 0
for i in range(N):
    if deg + A[i] < 360:
        deg += A[i]
        pizza_deg[i] = deg
    else:
        deg = deg + A[i] - 360
        pizza_deg[i] = deg
pizza_deg.sort(reverse=True)
for j in range(N):
    deg_diff[j] = pizza_deg[j] - pizza_deg[j + 1]
deg_diff.sort(reverse=True)
if N <= 2:
    if deg_diff[0] > 360 - deg_diff[0]:
        print(deg_diff[0])
    else:
        print(360 - deg_diff[0])
else:
    print(deg_diff[0])
