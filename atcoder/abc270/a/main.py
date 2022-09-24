# コードを記載
A, B = map(int,input().split())
ans_list = [4,2,1]
sunuke_list = []
for ans in ans_list:
    if A - ans >= 0 or B - ans >= 0:
        if A - ans >= 0:
            A -= ans
        if B - ans >= 0:
            B -= ans
        sunuke_list.append(ans)
print(sum(sunuke_list))
