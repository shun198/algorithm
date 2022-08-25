from collections import deque

N = int(input())
A = list(map(int, input().split()))

# マージソート本体
def merge_sort(v):
    # 配列が空の場合は何も起こらない
    if len(v) == 0:
        return

    # v[X] の値を軸に配列を分割する
    X = len(v) // 2
    L, R = v[:X], v[X:]

    # L, R を再帰的にソートする
    if len(L) >= 2:
        L = merge_sort(L)
    if len(R) >= 2:
        R = merge_sort(R)

    # L, v[X], R をこの順につなげ、もとの配列を更新する
    dq = deque()
    for l in L:
        dq.append(l)
    for r in reversed(R):
        dq.append(r)
    B = []
    while len(dq):
        if dq[0] <= dq[-1]:
            B.append(dq.popleft())
        else:
            B.append(dq.pop())
    return B


# マージソート
A = merge_sort(A)

# 配列の中身を出力する
print(*A)
