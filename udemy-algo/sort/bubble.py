from typing import List
import io
import sys


# 下記に標準入力を記載
_INPUT = """\
3 1 5 2 4
"""
sys.stdin = io.StringIO(_INPUT)

N = list(map(int, input().strip().split()))


def bubble_sort(num: List[int]) -> List[int]:
    len_num = len(num)
    for i in range(len_num):
        for j in range(len_num - 1 - i):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
    return num


print(bubble_sort(N))
