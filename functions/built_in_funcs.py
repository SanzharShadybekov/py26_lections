# Встроенные функции

# map
# filter
# lambda
# enumerate
# zip, all, any
# (reduce)


# Анонимные функции - lambda(такие же функции только без названия)
# lambda функции могуть принимать сколько угодно аргументов, но всегда вохвращают одно выражение

# def sum_of_args(a, b):
#     res = a + b
#     return res

# print(sum_of_args(1, 2))

# a = sum_of_args
# print(a(5, 15))

# sum_of_args2 = lambda a, b, c: sum([a, b, c])
# print(sum_of_args2(5, 15, 20))

# x = lambda a, b, c: (a * b) % c
# print(x(11, 5, 10))

# get_last = lambda ls: ls[-1]
# ls = [1,2,3,4,5,6,True, False, [123], 'last']
# print(get_last(ls))


# def myFunc(n):
#     return lambda a: a * n

# myDoubler = myFunc(2)
# myTripler = myFunc(3)
# print(myDoubler(50))
# print(myDoubler(100))
# print(myDoubler(23))
# print(myTripler(55))


# dict_ = {'John': 50_000, 'Sultan': 5, 'Jamie': 1000000000, 'Aigerim': 1_000_000}
# res = dict(sorted(dict_.items(), key=lambda x: x[1], reverse=True))
# print(res)

# ls = ['asdasfasfa', 'asda', 'asfasfas']
# res = sorted(ls, key=len)
# print(res)

# ------------------------------------

# map(function, iterable) - применяет функцию к каждому элементу из последовательности и возврщает mapobject(итератор) c результатом

# ls = ['one', 'two', 'three', 'four']
# for i in range(0, len(ls)):
#     ls[i] = ls[i].upper()
# print(ls)

# res = list(map(str.upper, ls))
# print(res)


# names = ['John', 'Sultan', 'Jamie', 'Raychel']
# # ['Hello mr/mrs John', 'Hello mr/mrs Sultan', ...]
# res = list(map(lambda name: f'Hello mr/mrs {name}', names))
# print(res)

dict_ =  {1: 2, 3: 4, 5: 6}
        # {1: '2', 3: '4', 5: '6'}

# for k in dict_:
#     dict_[k] = str(dict_[k])
# print(dict_)
# res = dict(map(lambda x: (x[0], str(x[1])), dict_.items()))
# print(res)

# --------------------------------
# filter(function, iterable) -> применяет ко всем элементам iterable функцию которую мы передали и возвращает итератор с теми элементами для которых фукнция вернула True 

# ls = ['one', 'two', '', 'list', '100', '1', 'john']
# res = []
# for x in ls:
#     if x.isdigit():
#         res.append(x)
# print(res)

# res = list(filter(str.isdigit, res))
# print(res)


# ls = ['john', 'makers', 'Sultan', 'ono', 'py.26', 'Kyrgyzstan', 'mountains']
# res = list(filter(lambda stroka: len(stroka) > 5, ls))
# print(res)


# ls = [
#     {'name': 'Python', 'point': 10},
#     {'name': 'C++', 'point': 6},
#     {'name': 'JS', 'point': 8},
#     {'name': 'JAVA', 'point': 3},
#     {'name': 'C#', 'point': 0},
# ]
# res = list(filter(lambda dict_: dict_['point'] >= 7, ls))
# print(res)

# users = [
#     {'username':'John', 'comments':['I love you', 'Really good']},
#     {'username':'Raychel', 'comments':[]},
#     {'username':'Steven', 'comments':['Bishkek', 'Python']},
#     {'username':'Hello', 'comments':[]},
#     {'username':'Kira', 'comments':['The best post']}
# ]
# inactive_users = list(filter(lambda dict_obj: not dict_obj['comments'], users))
# print(inactive_users)

# ----------------------------------------------

# names = ['Raychel', 'Sultan', 'Aigerim', 'John', 'Kira', 'Bob']
# new_names = list(
#     map(lambda name: f'Your name is {name}!', filter(lambda x: len(x) > 4, names))
# )
# print(new_names)

# -------------------------------------------------

# from functools import reduce

# ls = [1,2,3,4,5,6]
# sum_ = reduce(lambda a, b: a + b, ls)
# res = reduce(lambda a, b: a * b, ls)
# print(sum_)
# print(res)

# ----------------------

# ls = ['john', 'Sultan', 'Katana', 'Aigerim']
# for i, obj in enumerate(ls):
#     print(i , obj)
# print(enumerate(ls))

# -----------------------------------


# import string as s
# import random

# def generate_rand_str():
#     symbols = s.ascii_letters + s.digits
#     res = ''.join(random.choice(symbols) for i in range(0, 10))
#     return res

# print(generate_rand_str())
# print(generate_rand_str())
# print(generate_rand_str())
# print(generate_rand_str())
# print(generate_rand_str())

# --------------------------------------------
# from random import choices
# from string import ascii_letters, digits
# from itertools import repeat

# symbols = '_()$!%+-@#'
# q_pass = int(input('Vvedite kolichestvo paroley: ')) # 50

# result = {
#     f(choices(ascii_letters, k=10), choices(digits, k=5), choices(symbols, k=2)) for f in repeat(lambda x, y, z: ''.join(set(x+y+z)), q_pass)
# }
# print(result)
# print(f'Quantity of passwords: {len(result)}')

# from statistics import mean

# dlina = [len(x) for x in result]
# print(f'Average len: {mean(dlina)}')

# ----------------------------------------

# zip(iterables) - она соединяет каждый элемент итерируемых объектов между собой, по их распорядку, в тип данных tuple и возвращает его

# ls1 = [1, 2, 3, 4, 5, 6]
# ls2 = [100, 200, 300]

# res = list(zip(ls1, ls2))
# print(res)

# ls1 = [1, 2, 3, 4, 5]
# ls2 = [100, 200, 300, 400, 500]
# ls3 = [10 , 20, 30]

# res = list(zip(ls1, ls2, ls3))
# print(res)

# zip для создания словарей

# a = dict([(1, 2), (3, 4)])
# print(a)
# {1: 2, 3: 4}.items()
# dict_items[(1, 2), (3, 4)]


# d_keys = ['hostname', 'location', 'vendor', 'model', ' IOS', 'IP']
# d_values = ['apple_r1', 'wintefell', 'jobs', 'watch', '16.0', '10.255.0.1']

# i = 0
# res = {}
# for x in d_keys:
#     res[x] = d_values[i]
#     i += 1

# print(res)
# res = dict(zip(d_keys, d_values))
# print(res)


# d_keys = ['hostname', 'location', 'vendor', 'model', ' IOS', 'IP']
# data = {
#     'r1': ['london_r1', 'New Globe Walk', 'Cisco', '4451', '15.4', '10.255.0.1'],
#     'r2': ['london_r2', 'North London', 'Cisco', '5541', '16', '10.25.10.11'],
#     'sw1': ['london_sw1', 'South_West', 'Cisco', '3850', '16.4', '10.2.12.12']
# }

# print(data)
# for k in data:
#     data[k] = dict(zip(d_keys, data[k]))
# print()
# print(data)

# --------------------------------

# all(), any()

# all(iterable) - Возращает True, если все элменеты внутри объекта истинна, иначе возвразает False 

# all([1, 2]) -> True
# all([[]]) -> False
# all(['False', 'John', 5, 6, 1]) -> True
# all([[1,2,3], 5, None]) -> False

# print(all([[1,2], 5, 'stroka', True, 1, False]))
# print(all([[]]))


# ip = '10.10.10.10'
# result = all(i.isdigit() for i in ip.split('.'))
# print(result)


# any - возращает True, если хотябы один элемент истинна

# ls = [0, 0 , 0, '', False, 1]
# print(any(ls))

# ignore = ['rm -rf', 'reset', 'alias']
# command = input('vvedite commandu: ')
# sudo nano file
# sudo rm -rf file

# if any(word in command for word in ignore):
#     raise Exception('Invalid commmand')
# print('Vse ok!')










