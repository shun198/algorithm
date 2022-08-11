# 標準出力2-10
S = input()
N, M = map(int, input().split())
S_list = list(S)  # S を配列型に変換する
tmp = S_list[N-1]  # 一時変数に S_list[N-1] を代入する
S_list[N-1] = S_list[M-1]
S_list[M-1] = tmp
S = "".join(S_list)  # 配列の要素を結合して文字列型に変換する
print(S)
