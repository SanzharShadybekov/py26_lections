"""
Напишите класс Salary для расчета налогов на заработную плату. У класса должна быть обязательная переменная класса - процент налога от зарплаты - 15%. Объекты класса должны иметь сумму зарплаты и стаж работы в качестве атрибутов. Также у класса должен быть метод расчитывающий сумму налога заплаченного за весь стаж работы. Создайте экземпляр класса и посчитайте сумму вашего налога.
"""

# class Salary:
#     tax = 0.15

#     def __init__(self, salary, exp):
#         self.salary = salary
#         self.work_exp = exp
    
#     def sum_of_tax(self):
#         res = (self.salary * self.tax) * (self.work_exp * 12)
#         print(f'Сумма налогов составила {res} сомов, за {self.work_exp} лет!')

# john = Salary(170_000, 11)
# john.sum_of_tax()


# class Calc:
#     def add(self, a, b):
#         '''Function of sum'''
#         return a + b
 
#     def sqrt(self, num):
#         '''функция нахождения квадратного корня'''
#         import math
#         res = math.sqrt(num)
#         return round(res, 2)

#     def percent(self, num, percent):
#         '''функция нахождения процента от числа'''
#         return (num * percent) / 100
    
#     def super_func(self, string):
#         '''функция выполняет вычисления в строке'''
#         '1 + 1 + 2 + 3'
#         try:
#             return eval(string)
#         except:
#             return 'Invalid Operation'


# calc = Calc()
# print(calc.add(4, 5)) # 9
# print(calc.sqrt(9)) # 3
# print(calc.sqrt(2)) # 1.41
# print(calc.percent(87, 35)) # 30.45
# print(calc.percent(255, 25)) # 63.75
# print(calc.super_func('(5 - 7) ** 2 - 10')) # -6
# print(calc.super_func(input('Vvedite operaciyu: ')))


# class Sniper:
#     health = 100

#     def __init__(self, name) -> None:
#         self.name = name
    
#     def shoot(self, other):
#         other.health -= 20
#         print(f'Атаковал {self}')
#         print(f'Жертва: {other}, осталось здоровья: {other.health}')
    
#     def __str__(self) -> str:
#         return self.name

# sniper1 = Sniper('John')
# sniper2 = Sniper('Jamie')

# print(sniper1, sniper1.health)
# print(sniper2, sniper2.health)

# import random
# while sniper1.health and sniper2.health:
#     choice = random.randint(1, 2)
#     if choice == 1:
#         sniper1.shoot(sniper2)
#     else:
#         sniper2.shoot(sniper1)

# if sniper1.health:
#     print(f'{sniper1} победил!!!')
# else:
#     print(f'{sniper2} победил!!!')


# -------------------------------

# class CRUD:
#     __products = [] 
#     __id = 0

#     def _get_id(self):
#         self.__id += 1
#         return self.__id
    
#     def _get_product(self, id):
#         for x in self.__products:
#             if x['id'] == id: return x
#         return False

#     def create(self):
#         print('CREATE of product!')
#         title = input('Vvedite title: ')
#         price = input('Vvedite price: ')
#         self.__products.append({
#             'id': self._get_id(),
#             'title': title,
#             'price': price
#         })
    
#     def list_of_products(self):
#         print('Все наши продукты: ')
#         for x in self.__products:
#             print(x['title'])
    
#     def detail_product(self):
#         print('Detail:')
#         id = int(input('Введите ID продукта: ')) # 565
#         product = self._get_product(id)
#         print(product if product else 'Нет такого продукта!!')

#     def update_product(self):
#         print('Update:')
#         id = int(input('Введите ID продукта: ')) # 5
#         product = self._get_product(id)
#         if not product:
#             print('Нет такого продукта!')
#             return 
#         choice = input('Что изменить(title/price): ')
#         index = self.__products.index(product)
#         self.__products[index][choice] = input('Введите новое значение: ')
    
#     def delete_product(self):
#         print('DELETE:')
#         id = int(input('Введите ID продукта: '))
#         product = self._get_product(id)
#         if not product:
#             print('Нет такого продукта!')
#             return 
#         self.__products.remove(product)
#         print('Удалено!')


# product = CRUD()
# product.create()
# product.create()
# product.list_of_products()
# # product.detail_product()
# # product.detail_product()
# # product.update_product()
# # product.detail_product()
# product.delete_product()
# product.list_of_products()
