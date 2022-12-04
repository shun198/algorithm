# コードを記載
N, X, Y = map(int, input().split())
s = [input() for i in range(N - 1)]
tree_list = [1]
for i in range(len(s) - 1):
    tree_list.insert(0, s[i][0])
