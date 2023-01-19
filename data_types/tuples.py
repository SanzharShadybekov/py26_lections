# tuple() -> кортеж, неизменяемыый тип данных

# thistuple = (6,)
# print(thistuple)
# print(type(thistuple))

# mytuple = 'apple', 'pineapple', 'pan'
# print(mytuple)
# print(type(mytuple))


# a, b, c = 5, 10, 15
# print(a)
# print(b)
# print(c)

# for x in range(1, 5): # 1) x = 1
#     print(x)          # 2) x = 2  

# dict1 = {1: 'one', 2: 'two', 3: 'three'} 
# print(dict1.items())
# for x, y in dict1.items(): # 1) x = 1 y ='one'
#     print(x, y)

# a = [(1, 2), (3, 4), (5, 6)]
# for x, y in a:
#     print(x, y)

# ls = list(range(1, 100_001))
# tp = tuple(range(1, 100_001))
# print(tp)
# print(len(tp))
# print('LIST', ls.__sizeof__())
# print('TUPLE', tp.__sizeof__())

# tuple_ = (1,2,3,4,5) #неизменяемый
# del tuple_[-1]
# print(tuple_)

# ls = [1,2,3,4,5]
# del ls[-1] 
# print(ls)

# print(dir(tuple))
# tuple_ = (1,2,3,4,5,6,7,8,2,2,2,2,2)
# print(tuple_.index(5))
# print(tuple_.count(2))

# tp = ('apple', 'cherry', 'banana', 'john')
# for x in tp:
#     print(x)
#     print(x * 3)
# i = 0
# while i < 50:
#     print(i)
#     i += 1 # инкримент i = i + 1
#            # дикремент i -= 1

# tp = ('apple', 'cherry', 'banana', 'john')
# x = 0
# while x < len(tp):
#     print(tp[x], f'index: {x}') 
#     x += 1

# + *
# a = (1,2,3) # '123' * '456' = '123456'
# b = (4,5,6)
# print(a * 5)
# print('123' * 5)

# c = (5,)
# a = ()
# # c += c
# # print(c)
# for x in range(1, 101):
#     a += c

# print(a)


# 1) input:
# tp = (1,8,3,4,5,8,8,9,2)
# target = 8
# output: result = (8,3,4,5,8)

# 2) input
# tp = (1,2,3,8,5,1,2)
# target = 8
# output: result = (8,5,1,2)


# tp = (1,2,3,8,5,1,2)
# target = 2

# if tp.count(target) > 1:
#     first = tp.index(target)
#     second = tp.index(target, first+1)
#     result = tp[first: second + 1]
# else:
#     first = tp.index(target)
#     result = tp[first:]
# print(tp, target)
# print(result)

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# 1) nums = [2,7,11,15]
# target = 9
# result = [0, 1] --- 2 + 7 = 9
                    # 9 - 2 = 7
                    # 9 - 7 = 2
# 2) nums = [4, 11, 2, 5, 1, 6]
# target = 8         # 8 - 2 = 6
# result = 2 5

# nums = [4, 11, 2, 5, 1, 6]
# target = 9

# for x in nums:
#     num = target - x
#     if num in nums:
#         if num == x:
#             continue
#         print(nums.index(x), nums.index(num))
#         break





