import json

# 1․ Գրել հետևյալ ծրագիրը․
#    - բացել jupyter notebook-ը,
#    - գեներացնել list, որը կպարունակի 1-ից 1000000 միջակայքում գտնվող կենտ թվերը,
#    - պահել գեներացված list-ը համապատասխան ֆորմատով համակարգչի մեջ data անունով,
#    - բացել pycharm-ը,
#    - pycharm-ում կարդալ data ֆայլը,
#    - կարդացած list-ում կթողնի միայն 3-ի բաժանվող թվերը,
#    - կտպի ստացված list-ի արժեքների միջին թվաբանականը։

f = open('homework23.json', 'r')
data_2 = json.load(f)
data_3 = [i for i in data_2 if i % 3 == 0]
f.close()
print(data_3)

# 2․ Գրել ծրագիր, որը․
#    - հետևյալ dict_1-ից կստանա նոր dict_2 այնպես, որ dict_2-ի key-երը լինեն dict_1-ի value-ները, իսկ value-ները՝ dict_1-ի value-ների երկարությունները,
#    օրինակ՝ dict_1 = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'},
#    պետք է ստացվի՝ dict_2 = {'red': 3, 'green': 5, 'black': 5, 'white': 5}:
#
# dict_1 = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# dict_2 = {}
# for i in dict_1.values():
#     dict_2.update({i: len(i)})
# print(dict_2)
#
# 3. Գրել ֆունկցիա, որը․
#    - կֆիլտրի տրված dictionary-ի value-ները, թողնելով միայն կենտ թվերը,
#    - կվերադարձնի ստացված dictionary-ն,
#    օրինակ՝ {'a': [1, 8, 3, 7, 2], 'b': [12, 4, 8, 4], 'c': [9, 9, 2, 8, 5]},
#    պետք է ստացվի՝ {'a': [1, 3, 7], 'b': [], 'c': [9, 9, 5]}:
#
# dict_1 = {'a': [1, 8, 3, 7, 2], 'b': [12, 4, 8, 4], 'c': [9, 9, 2, 8, 5]}
# dict_2 = {}
# for i in dict_1.values():
#     for a in i.copy():
#         if a % 2 != 1:
#             i.remove(a)
# print(dict_1)