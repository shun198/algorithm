X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
cnt = 0
for a_item in A:
    for b_item in B:
        for c_item in C:
            if a_item + b_item == c_item:
                cnt += 1
print(cnt)
