# コードを記載
dots = [""] * 10
cnt = 1
A = 0
B = 0
C = 0
D = 0
# S個分代入していく
for i in range(10):
    dots[i] = input()

for items in dots:
    if len(items.strip(".")) == 0:
        if A != 0:
            B = cnt -1
            break
        cnt += 1
        continue
    else:
        if A == 0:
            A = cnt
            C = 10 - len(items.lstrip(".")) + 1
            D = len(items.rstrip("."))
        cnt += 1
if B == 0:
    B = 10
        
print(A,B)
print(C,D)
    
        
