# コードを記載
# Xがゴール
# Yに壁
# Zにハンマー
X, Y, Z = map(int, input().split())
# Yが0より低く、0からゴールまでに壁がないとき
if X > 0 and Y < 0:
    print(X)
elif X > 0 and X > Y:
    # ハンマーが壁の前にある時
    if Y > Z:
        if Z > 0:
            print(X)
        elif Z < 0:
            print(abs(Z) * 2 + X)
    else:
        print(-1)
elif X > 0 and X < Y:
    print(X)
elif X < 0 and Y > 0:
    print(abs(X))
elif X < 0 and X < Y:
    # ハンマーが壁の前にある時
    if Y < Z:
        if Z < 0:
            print(abs(X))
        elif Z > 0:
            print(abs(Z) * 2 + abs(X))
    else:
        print(-1)
elif X < 0 and X > Y:
    print(abs(X))
