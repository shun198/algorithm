# https://ta7uw.hatenablog.com/entry/2019/02/24/165740
from itertools import accumulate

a_list = [i for i in range(10)]
print(a_list)
a_acc = list(accumulate(a_list))
print(a_acc)

b_list = [20, 14, 34, 65, 130, 15, 2, 28, 68, 45]
print(b_list)
b_acc = list(accumulate(b_list, min))
print(b_acc)
# [20, 14, 14, 14, 14, 14, 2, 2, 2, 2]

from itertools import accumulate

c_list = [20, 14, 34, 65, 130, 15, 2, 28, 68, 45]
print(c_list)
c_acc = list(accumulate(c_list, max))
print(c_acc)
# [20, 20, 34, 65, 130, 130, 130, 130, 130, 130]
