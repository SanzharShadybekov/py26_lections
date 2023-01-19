# def sum_of_args(a, b, c, d): #params
#     return a + b + c + d

# result = sum_of_args(5, 10, 25, 20)
# print(result)
# print(result(5, 10, 15, 20))

# ----------------------
# позиционные и именованные аргументы

# def printParams(a=None, b=None, c=None):
#     print(a, 'is stored in param a')
#     print(b, 'is stored in param b')
#     print(c, 'is stored in param c')

# printParams(a=5, c=10)

# def sum_of_args(a, b, c, d): #params
#     return a + b + c + d

# print(sum_of_args(5, 10, 15, 20)) # arguments (позиционные аргументы)
# print(sum_of_args(a=5, c=15, d=20, b=10)) # keyword arguments (Именованные аргументы)
# print(sum_of_args(5, 10, d=20, c=15))

# ---------------------------
# оператор *
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = [*a, *b]
# print(c)

# -----------------------
# *args **kwargs в функциях

# def printScores(student, *scores):
#     print(f'Student name: {student}')
    # print(*scores)
#     # print(type(scores))
#     # ls = list(scores)
#     for x in scores:
#         print('Score:', x)

# printScores('John Snow', 100, 99, 95, 90)

# def print_pet_names(owner, **pets):
#     print(f'Owner name: {owner}')
#     # print(pets)
#     # print(type(pets))
#     for pet, name in pets.items():
#         if type(name) == list:
#             print(f'{pet}:', *name)
#         else:
#             print(f'{pet}: {name}')

# print_pet_names('John Snow', dog='Rex', cat='Garfild', fish=['Nemo', 'Dori', 'Alex'], turtle='Leonardo')


# def get_some_data(a, b, *args, **kwargs):
#     print('Параметры a и b:', a, b)
#     print('Аргументы:', args)
#     print('Именованные аргументы:', kwargs)
#     print(args[0])
#     print(args[-1])
#     print(kwargs['name'])

# get_some_data(1, 2, 3, 4, 5, lang='Python', name='John Snow', car='BWM M8')

# ---------------------------------
# def generate_random_string(len_):
#     import string  as s
#     import random
#     random_str = ''.join(
#         random.choice(s.ascii_letters + s.digits) for i in range(0, len_)
#         )
#     return random_str

# print(generate_random_string(25))

# ---------------------------
def add(a, b): return a + b

def subtract(a, b): return a - b

def multiply(a, b): return a * b

def divide(a, b):
    try: 
        return a / b
    except ZeroDivisionError:
        return 'На ноль делить нельзя!'

def calc(num1, num2):
    operator = input('Введите оператор(+,-,*,/): ')
    if operator == '+': return add(num1, num2)
    elif operator == '-': return subtract(num1, num2)
    elif operator == '*': return multiply(num1, num2)
    elif operator == '/': return divide(num1, num2)
    else: return 'Вы ввели неверный оператор!'

def main():
    try:
        num1 = float(input('Введите первое число: '))
        num2 = float(input('Введите втоорое число: '))
    except ValueError:
        print('Вы ввели некоректные даннные')
        main()
        return 
    
    while True:
        result = calc(num1, num2)
        if type(result) == float:
            print(f"Result: {result}")
            break
        else:
            print(f"Result: {result}")

    question = input('Хоите продолжить(Yes/No)? ')
    if question.lower() == 'yes':
        main()
    else:
        print('Спасибо за использования нашего калькулятора! Пока!')


if __name__ == "___main___":
    main()
