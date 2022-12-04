# コードを記載
# コードを記載
import io
import sys
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

# 下記に標準入力を記載
_INPUT = """\
2048 2

"""
sys.stdin = io.StringIO(_INPUT)

X, K = map(int, input().split())

for i in range(K):
    if (X % pow(10, i + 1)) >= 5:
        print(X)
print(X)
