
# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]] 


# if len(lists) == 1:
#     print(f'max_list {lists[0]}')
#     print(f'min_list {None}')
# else:
#     list_of_len = []
#     for x in lists:
#         list_of_len.append(len(x))

#     min_value = min(list_of_len)
#     max_value = max(list_of_len)
#     if min_value == max_value:
#         max_index = list_of_len.index(max_value)
#         print(f'max_list {lists[max_index]}')
#         print(f'min_list {None}')
#     else:
#         min_index = list_of_len.index(min_value)
#         max_index = list_of_len.index(max_value)
#         print(f'max_list {lists[max_index]}')
#         print(f'min_list {lists[min_index]}')



lists = [[0], [1, 3], [100, 7], [9, 11], [13, 15, 17]] 

max_value = max(lists, key=len)
min_value = min(lists, key=len)

if max_value == min_value:
    print(f'max_list {max_value}')
    print(f'min_list {None}')
else:
    print(f'max_list {max_value}')
    print(f'min_list {min_value}')

    