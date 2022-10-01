# コードを記載
line = input().split()
num = int(line[0])
queries = int(line[1])
numbers = input().split()
map = {}

for n in range(num):
    key = int(numbers[n])
    if key in map:
        map[key].append(n)
    else:
        map[key] = [n]

for i in range(queries):
    line = input().split()
    x = int(line[0])
    k = int(line[1])
    if x in map:
        if k <= len(map[x]):
            print(map[x][k - 1] + 1)
            continue
    print("-1")
