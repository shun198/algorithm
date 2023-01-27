# コードを記載
A, B = map(int, input().split())
# A-(A*0.08)からA+(A*0.08)までってこと？
yen = 0

for i in range(int(A / 0.1), int(B / 0.08) + 1):
    if i * 0.08 >= A:
        yen = i
        continue
    else:
        break
print(yen)
