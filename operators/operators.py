# Операторы сравнения 
# Условные операторы
# Логические операторы

# операторы сравнения
# <, >, ==, <=, >=, !=(не равно)
 
# num1 = 18
# num2 = 18
# print(num1 >= num2)
# stroka1 = 'Aaaaa!'
# stroka2 = 'Aaaab!'
# print(stroka1 == stroka2)
# print(ord('H'))
# print(ord('W'))
# print(chr(1100))

# text = 'Hello world! My name is John!'

# if ord(text[5]) == 72:
#     print('Yes!')
# else:
#     print('Nooo!')

# условные операторы - они созданы, чтобы программа могла выполнять разные участки кода в зависимости от условия
# if, elif, else

# if <condition>:
#     <body if> #сработает только если true
# elif <condition>:
#     <body elif>
# elif <condition>:
#     <body elif>
# else:
#     <body else> #сработает только если во всех остальных false

# string = input('Enter smt: ')

# if string == 'Hello':
#     print('Hello stranger!')
# elif string == 'John':
#     print('Welcome back John Snow!')
# elif string == 'Mercedez':
#     print('Mersedez Benz S class!')
# else: 
#     print('совпадений не найдено')

# print('The end!')

# email = input('Enter Email: ')
# password1 = input('Enter password: ')

# if len(password1) < 8:
#     raise Exception('Password too short! (password need at least 8 characters!)')
    

# password2 = input('Enter password confirmation: ')

# if password1 != password2:
#     raise Exception('Passwords did\'t match!')
# else:
#     print('Successfully signed up!')

# age = input('Enter your age: ')

# if age.isdigit():
#     age  = int(age)
#     print(f'Your age: {age}!')
# else:
#     raise Exception('Enter the valid age(only digits!)')

# if age > 170:
#     raise Exception('Invalid age!')

# if age < 21:
#     print(f'Chuvak prihodi cherez {18 - age} let/goda!')
# else:
#     print('Ty prohodish\' po vozrastu, Welcome!')

# логические операторы
# and -> логическое и
# or  -> лог или
# not -> лог отрицание

# операторы идентификации
# in -> проверят наличие элемента внутри массива либо строки
# is -> сравнивает ячейки памяти
#   ==  сравнивает значения
# is not -> отрицательное сравнение двух ячеек

# my_age = 20
# other_age = 18
# result = my_age == 21 or other_age == 19
#         #  FALSE             #  FALSE    
#                   # FALSE
# print(result)

# result = not my_age == 20
#             # TRUE
# print(result)

# cash = int(input('Enter your cash: '))

# if cash > 1000 and cash < 10000:
#     print('Sredne!')
# elif cash >= 10000 and cash < 100_000:
#     print('mnogo!')
# elif cash >= 100_000:
#     print('krasavchik!')
# else:
#     print('pechal\'no!')


# is_google_user = True
# is_github_user = True
# is_age_less_21 = True
# user_coin = 3000

# if (is_google_user or is_github_user) and (is_age_less_21 or user_coin > 5000):
#     print('You enter the system')
# else:
#     print('Sorryy, you couldn\'t enter!')

str1 = 'Hello world!'
choice = input('Enter the character: ')

if choice in str1:
    print(f'Символ {choice} есть в строке: "{str1}"!')
else:
    print(f'Символа {choice} нет в строке: "{str1}"!')

