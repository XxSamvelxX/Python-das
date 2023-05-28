import string

# 1․ Գրել ֆունկցիա, որը․
# - տրված բառերի list - ը կֆիլտրի այնպես, որ կթողի միայն ամենաերկար բառերը
# (այսինքն՝ կգտնի ամենաերկար բառի երկարությունը և լիստում կթողնի միայն այդ երկարության բառերը),
# օրինակ՝ input = ["aba", "aa", "z", "ad", "vcd", "aba"]
# output = ["aba", "vcd", "aba"],
# input = ["aba", "aa", "z", "advc", "vcd", "aba"]
# output = ["advc"],
# - վերջում գնահատեք Ձեր գրած կոդը Big O notation - ի միջոցով։

# l_1 = ['qwer', 'qwert', 'qwe', 'qwert', 'asd', 'asdf', 'asdfg', 'zxcv', 'zxcvb']
# # ['qwert', 'qwert', 'asdfg', 'zxcvb', 'qwer', 'asdf', 'zxcv', 'qwe', 'asd']
# l_1.sort(key=len, reverse=True)
# for i in range(0, len(l_1) + 1):
#     if len(l_1[i]) == len(l_1[i + 1]):
#         print(l_1[i])
#     else:
#         print(l_1[i])
#         break

# Big O(n)

# 2․ Գրել ֆունկցիա, որը․
# - կհաշվի, թե տրված ամբողջ թվերի list - ից քանի քայլով կարելի է ստանալ մոնոտոն աճող թվերից բաղկացած list,
# մեկ քայլի ընթացքում թույլատրվում է թվերից մեկը մեկով մեծացնել, թվերի տեղերը փոխել չի կարելի,
# օրինակ՝ [-10, 0, -2, 0] -> 5,
# [1, 1, 1] -> 3:

# l_1 = [-10, 0, -2, 0]
# count = 0


# 3. Գրել ֆունկցիա, որը․
# - կստանա երկու արգումենտ՝ a և b, - կվերադարձնի a - ի b աստիճանի ամենավերջի թվանշանը,
# փորձել խնդիրը լուծել այնպես, որ կոդը աշխատի շատ արագ՝ նույնիսկ շատ մեծ թվերի դեպքում։

# def x(a, b):
#     a = a % 10
#     b = b % 10
#     return a ** b
#
#
# print(x(1223413134454124513173623, 1231782623242511341315431))

# Ex 5
# Caesar cipher

# l_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# l_2 = ['e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd']
# # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# text = "Barev axper, kod@ pti ashxati"
# text_1 = ""
# for i, j in zip(text, l_2):
#     if i.lower() in l_1:
#         print(i, j)
#         text_1 += j
#     elif i in string.punctuation or i == " ":
#         text_1 += i
# print(text_1)
# print(text)
