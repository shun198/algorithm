# https://ta7uw.hatenablog.com/entry/2019/02/24/165740
import bisect

A = [1, 2, 3, 3, 3, 4, 4, 6, 6, 6, 6]
print(A)
left_index = bisect.bisect_left(A, 3)  # 2 最も左(前)の挿入箇所が返ってきている
print(left_index)
right_index = bisect.bisect_right(A, 4)
print(right_index)
A.insert(left_index, 3)
print(A)  # [1, 2, 3, 3, 3, 4, 4, 6, 6, 6, 6]

# 探索範囲を絞り込む
A = [1, 2, 3, 3, 3, 0, 0, 0, 0, 0, 0]
index = bisect.bisect_left(A, 3, 0, 5)
print(index)  # 2


A = [1, 2, 3, 3, 3, 4, 4, 6, 6, 6, 6]
bisect.insort(A, 3)  # [1, 2, 3, 3, 3, 3, 4, 4, 6, 6, 6, 6]
