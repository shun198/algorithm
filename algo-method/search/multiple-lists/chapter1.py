N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = 0
for a_item in A:
    for b_item in B:
        if a_item > b_item:
            cnt += 1
print(cnt)
