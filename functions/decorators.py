# фукнция высшего порядка - это функция которая в качестве аргумента принимает другую функцию

# Декоратор - это функция, которая позволяет без изменения кода обренуть другую фукнцию для того чтобы расширить фукнционла обернутой фукнции

# def decorator(func): 
#     print(f'Called Func name: {func.__name__}') # 2
#     return func() # 3: call func # 6 retun 'Hello'

# def hello():
#     print('Vsem privet!') # 4
#     return 'Hello' # 5

# def john():
#     print('Hello my name is John Snow!')
#     return 'John Snow'

# # hello()
# # john()
# a = decorator(hello) # вызов # 1
# b = decorator(john)
# print(a, b)
# from typing import Callable


# def benchmark(func: Callable):
#     import time
#     start = time.time()
#     res = func()
#     finish = time.time()
#     print(f'Время выполнения фукнции {func.__name__}: заняло {finish - start}')
#     return res

# def loop():
#     i = 1
#     range_number = 100_000
#     while i < range_number:
#         # print(i)
#         i += 1
#     return i

# print(benchmark(loop))


# Pythonic way -> @decorator
# Синтаксический сахар -> это красота кода
# from typing import Callable

# def benchmark(func: Callable):
#     def wrapper(): # 2
#         import time
#         start = time.time()
#         res = func() # 3
#         finish = time.time()
#         print(f'Время выполнения фукнции {func.__name__}: заняло {finish - start}')
#         return res
#     return wrapper

# @benchmark
# def loop(): # 4
#     i = 0
#     range_number = 1_000_000
#     while i < range_number:
#         i += 1
#     return i

# @benchmark
# def add():
#     i = 0
#     range_number = 1_000_000
#     ls = []
#     while i < range_number:
#         i += 1
#         ls.append(i)
#     return ls

# print(loop()) # 1
# add()

# def strong(func):
#     def wrapper(*args, **kwargs):
#         return '<strong>' + func() + '</strong>'
#     return wrapper

# def div(func):
#     def wrappper(*args, **kwargs):
#         return '<div>' + func() + '</div>'
#     return wrappper


# @div
# @strong
# @div
# def john():
#     return 'John Snow'

# print(john())


# def trace(func):
#     def wrapper(*args, **kwargs):
#         print(f'Trace: вызвана {func.__name__}(),\n{args} {kwargs}')
#         original_result = func(*args, **kwargs)
#         print(f'Trace: вызвана {func.__name__}(),\nвернула {args} {kwargs}')
#         return original_result
#     return wrapper

# @trace
# def say(name, line):
#     return f'{name}: {line}'

# print(say('John', 'Snow'))


# def func():
#     print('hello world')
#     return func


# def func1():
#     pass

# def func2(func1):
#     pass



# filter
# map














