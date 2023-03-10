# "====================Pytest========================="

# "TESTS - это проверка вашего кода, тесты бывают ручного типа и автотесты" 

# "pytest - это библиотека, для тестирования кода"

# "===============Запуск тестов====================="

# #pytest - запуск тестов с текущей директории и всех дочерних

# #pytest test_name.py - запуск определенного теста

# #pytest test_name.py::test_1 - запуск определенной тест-функции в определенном файле 

# '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
# "Названия всех файлов с тестами должна начинаться на test_название.py, либо название_test.py"

# "Названия тест-функций должно начинаться с test_название"
# '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'


# '====================================================================='
# #миниПРАКТИКА
# import pytest

# def oper(a, b):
#     return a / b 

# '------------------------------1вариант---------------------------------'
# #так писать плохо
# @pytest.mark.skip(reason='не завершен') # пропускает эту тест-функцию 
# def test_oper():
#     assert oper(10, 5) == 2
#     assert oper(20, 5) == 4
#     assert oper(10, 2) == 5
#     assert oper(0, 1) == 0


# '---------------------------2вариант----------------------------'
# #так писать плохо
# def test_oper_1():
#     assert oper(10, 5) == 2

# def test_oper_2():
#     assert oper(20, 5) == 4

# def test_oper_3():
#     assert oper(10, 2) == 5

# def test_oper_4():
#     assert oper(0, 1) == 0

# '-------------------------3вариант-----------------------------------'
# #отличный вариант
# @pytest.mark.parametrize('num1, num2, result', [(10, 5, 2),
#                                                 (20, 5, 0),
#                                                 (10, 2, 5),
#                                                 (0,1,0)])
# def test_oper_5(num1, num2, result):
#     assert oper(num1, num2) == result


# '----------------------Обработка исключений---------------------------'
# #плохой способ
# def test_oper_zero():
#     with pytest.raises(ZeroDivisionError):
#        oper(10,0)

# def test_oper_str():
#     with pytest.raises(TypeError):
#         oper(10,'str') 

# '---------------'
# #хороший способ
# @pytest.mark.parametrize('a, b, error', [(10, 'str', TypeError),
#                                         (10, 0, ZeroDivisionError)])
# def test_oper_error(a, b, error):
#     with pytest.raises(error):
#         oper(a, b)



from datetime import date

# print(date(2023, 2, 30))

month = 2
ls = []
for x in range(32):
    try:
        ls.append(date(2023, month, x))
    except ValueError:
        pass

print(ls)

