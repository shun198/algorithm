def prime_numbers():
    numbers = [True for i in range(201)]
    for i in range(2, 201):
        if numbers[i] is True:
            for x in range(i * 2, 201, i):
                numbers[x] = False
    return numbers


primes = prime_numbers()

line = input().split(" ")
a = int(line[0])
b = int(line[1])
c = int(line[2])
d = int(line[3])

aoki = True
for x in range(a, b + 1):
    aoki = False
    for y in range(c, d + 1):
        if primes[x + y] is True:
            aoki = True
            break
    if aoki is False:
        break
if aoki:
    print("Aoki")
else:
    print("Takahashi")
