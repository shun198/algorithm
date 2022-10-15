# コードを記載
N = int(input())

def recursive(number):
    if number == 0:
        return 1
    else:
        return recursive(number-1)*number

print(recursive(N))
