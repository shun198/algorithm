# 標準出力3-9
N = int(input())  # 入力を整数型として受け取る
A = [""] * N
for i in range(N):
    A[i] = input()  # 入力を文字列型配列として受け取る
ans = ""  # 答え
for item in A:  # A の各要素の頭文字をつなげる
    ans += item[0]
print(ans)
