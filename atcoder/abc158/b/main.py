# コードを記載
N, A, B = map(int, input().split())
# N // (A+B) * A → Aの個数を求める
# min(N % (A+B), A) → 余ったボールの個数を求める
print(N // (A + B) * A + min(N % (A + B), A))
