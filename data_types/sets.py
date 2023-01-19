# Множество в пайтоне - "контейнер", который содержит в себе уникальные элементы в неупорядоченном виде

# {} !!!! dict
# set()
# a = {'a': 1} -> словарь
# a = {1, 2, 3} -> множество

# set1 = {8, 1, 1, 1, 1, 1, 1, 2, 3, 4, 11}
# print(set1)
# print(type(set1))

# ls = ['Hello', 'Hello', 'hello', 'John', 'Snow', 'John']
# print(ls)
# res = set(ls)
# print(res)
# res = list(res)
# print(res)
# print(type(res))

# ls = [1, 2, 4, 'a', False, True, 'n', 'b']
# str1 = 'Hello world'
# ls.extend(str1)
# # print(ls)
# res = set(ls)
# print(res)


# FIFO / LIFO
# set1 = {1,2,3,4,5,6,7,8,9}
# set1.pop()
# print(set1)

# remove/discard
# remove -> error
# discard -> None
# set1 = {1,2,3,4,5}
# set1.remove(20) #error
# set1.discard(25) #нет ошибки
# set1.add(15)
# print(set1)

#frozenset
# a = set([1,2,3,4,5])
# b = frozenset([1,2,3,4,5])
# print(a, type(a))
# print(b, type(b))

# Создайте кортеж из 8-ми кортежей учащихся ВУЗов. В кортеже будут присутствовать следующие поля: имя студента, возраст, оценка за семестр, город проживания. Ваш код будет принимать этот кортеж, вычислять среднюю оценку по всем учащимся и выводить на печать следующее сообщение: “Ученики {список имен студентов через запятую} в этом семестре хорошо учатся!”. В список студентов, которые выводятся по результатам работы функции, попадут лишь те, у которых оценка за семестр равна или выше средней по всем учащимся.

# кортеж(имя, возраст, оценка, город)
students = (
    ('Елена', '13', 9, 'Москва'),
    ('Ольга', '11', 7.9, 'Иваново'),
    ('Елизавета', '14', 9.1, 'Тверь'),
    ('Дмитрий', '12', 5.2, 'Челябинск'),
    ('Максим', '15', 6.1, 'Самара'),
    ('Николай', '11', 8.7, 'Владивосток'),
    ('Артур', '13', 5.8, 'Екатеринбург'),
    ('John', '13', 10, 'WinterFell')
)
marks = []
for x in students:
    marks.append(x[2])

print(marks)
avg_mark = sum(marks) / len(marks)
print(avg_mark)

good_students = {}
for student in students:
    if student[2] > avg_mark:
        good_students.update({student[0]: student[2]})

str1 = f'{good_students}'
print(f"Ученики {str1[1:-1]} в этом семестре хорошо учатся!")





