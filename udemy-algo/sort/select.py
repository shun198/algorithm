from typing import List
import io
import sys


# 下記に標準入力を記載
_INPUT = """\
4 1 3 2 5
"""
sys.stdin = io.StringIO(_INPUT)

N = list(map(int, input().strip().split()))


def select_sort(num: List[int]) -> List[int]:
    len_num = len(num)
    for i in range(len_num):
        index = i
        for j in range(i+1,len_num):
            if num[index] > num[j]:
                index = j
        num[i],num[index] = num[index],num[i]
    return num


print(select_sort(N))
