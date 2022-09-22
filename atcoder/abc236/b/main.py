# # コードを記載
N = int(input())
A = list(map(int, input().split()))
# # A_set = set(A)
# # for items in A_set:
# #     if A.count(items) != 4:
# #         print(items)
# #         break
count = [0] * N
for x in A:
    count[x - 1] += 1

print(count.index(3) + 1)
# num1 = [1, 3, 2, 5, 4]
# num2 = {1, 3, 6}
# for num in num2:
#     if num in num1:
#         print("Yes")
#     else:
#         print("No")
# algo1 = ["a", "l", "g", "o"]
# algo2 = {"a", "r", "t"}
# for algo in algo2:
#     if algo in algo1:
#         print("Yes")
#     else:
#         print("No")
