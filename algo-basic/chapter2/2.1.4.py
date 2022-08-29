# # 2進数から10進数
# print(int("1001", 2))
# # 10進数から2進数
# print(format(127, "b"))


# def base_n(num_10, n):
#     str_n = ""
#     while num_10:
#         if num_10 % n >= 10:
#             return -1
#         str_n += str(num_10 % n)
#         num_10 //= n
#     return int(str_n[::-1])


# def ten_to_n(num_10, num):
#     if num >= 10 or num <= 1:
#         return "numの引数は1以上9以下にしてください"
#     answer = ""
#     while num_10 >= num:
#         if num_10 % num == 0:
#             answer += "0"
#         else:
#             answer += str(num_10 % num)
#         num_10 = num_10 // num
#     answer += str(num_10)
#     return answer[::-1]


# print(base_n(3429, 3))
# print(ten_to_n(3429, 1))


# def base_10(num_n, n):
#     num_10 = 0
#     for s in str(num_n):
#         num_10 *= n
#         num_10 += int(s)
#     return num_10


# print(base_10(102204, 5))
# print(int("102204", 5))

# print(format(100, "x"))
# print(int("64", 16))

# print(abs(-10))
# print(pow(4, 3))
from math import sqrt

print(sqrt(2))
