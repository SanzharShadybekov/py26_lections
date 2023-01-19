# Обработка исключений
# Oператор try except

# ошибки -> связаны с кодом
# SyntaxError
# IndentationError
# TabError

# исключения -> Invalid values
# ZeroDivisionError
# ArithmeticError
# NameError
# KeyError
# IndexError
# ValueError
# ImportError
# BaseException #прородитель всех исклчюений

# try except

# try:
    # <body try>
# except <Exception>:
    # <body>
# <else>:
    # <body> Только если все окей
# <finally>: 
    # <body> в любом случае в конце

# num1 = int(input('Vvedite chislo: '))
# print(num1)
# print('Important!')

# try:
#     num1 = int(input('Vvedite chislo: '))
# except ValueError:
#     print('Invalid Value')
# else:
#     print(num1)
# finally:
#     print('Important!')


# try:
#     num1 = int(input('Vvedite 1oe chislo: '))
#     num2 = int(input('Vvedite 1oe chislo: '))
#     print(num1 / num2)
# except (ValueError, ZeroDivisionError) as error:
#     print('Vy vveli nekorektnye dannye!')
#     print(error)

# try:
#     num1 = int(input('Vvedite 1oe chislo: '))
#     num2 = int(input('Vvedite 1oe chislo: '))
#     print(num1 / num2)
# except Exception as error:
#     print('Vy vveli nekorektnye dannye!')
#     print(error)

# list_ = [1,2,3,4,5]
# try: 
#     index = int(input('Vvedite index: '))
#     res = list_[index]
#     print(res)
# except ValueError:
#     print('Value error!')
# except IndexError:
#     print('Index error!')

# try:
#     num1 = int(input('Enter: '))
#     num2 = int(input('Enter: '))
#     result = num1 / num2
# except ZeroDivisionError:
#     print('na 0 delit\' nal\'zya!')
# except ValueError:
#     print('invalid symbols for int()!')
# else:
#     print(result)
# finally:
#     print('The End!')
