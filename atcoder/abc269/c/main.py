# コードを記載
N = int(input())
N_two_bit = int(format(N, "b"))
N_rev = ~N
N_rev_two_bit = format(N_rev * (-1), "b")
N_rev_two_bit = N_rev_two_bit[1:]
for i in range(N + 1):
    if i != (i | int(N_rev_two_bit, 2)):
        print(i)
