# # コードを記載
# S = input()
# # S.append(S[0])
# word_list = list(S)
# word_rev_list = list(reversed(S))

# word_list_with_a = list(S)
# word_list_with_a.insert(0, "a")
# word_rev_list_with_a = list(reversed(word_list_with_a))
# # print(word_rev_list)
# if word_list == word_rev_list or word_list_with_a == word_rev_list_with_a:
#     print("Yes")
# else:
#     print("No")
S = input()
first = len(S)
first = first - len(S.lstrip("a"))
last = len(S)
last = last - len(S.rstrip("a"))
# print(S.lstrip("a"))
# print(S.rstrip("a"))

if last < first:
    print("No")
else:
    add = "a" * (last - first) + S

    if add == add[::-1]:
        print("Yes")
    else:
        print("No")
