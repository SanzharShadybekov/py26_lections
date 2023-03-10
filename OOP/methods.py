# существует 3 вида методов
# class methods, instance methods, static methods


# instance methods - обычные методы, которые принимают первым аргументом self (ссылка на объект). Нужны они для того чтобы внутри метода мы согли работать с аттрибутами объекта.

# class A:
#     def instance_method(self, a):
#         print('метод объекта')
#         print('первый аргумент:', self)

# obj_a = A()
# obj_a.instance_method(5) # если вызываем у объекта, то self передается автоматически
# A.instance_method(obj_a, 5) # если вызываем у класса, то в self нужно передать объект в ручную


# class methods - методы, которые принимают первым аргументом cls (ccылка на класс). Нужны они для создания объектов или измнения аттрибутов класса. Для того чтобы создать класс метод нужно воспользоваться декоратором @classmethod

# class B:
#     @classmethod
#     def class_method(cls, a):
#         print('класс метод')
#         print('первый аргумент:', cls)

# obj_b = B()
# print(B, '!')
# obj_b.class_method(5)
# B.class_method(5)

# class C:
#     counter = 0

#     def __init__(self) -> None:
#         self._inc_counter()
#         self.a = 4

#     @classmethod
#     def _inc_counter(cls):
#         cls.counter += 1

# obj1 = C() # 1
# obj2 = C() # 2
# obj3 = C() # 3
# obj3.counter = 3
# obj4 = C() # 4
# print(obj3.counter)
# print(obj1.counter)
# print(obj4.counter)
# print(C.counter)


# class Pizza:
#     def __init__(self, radius, *ingredients) -> None:
#         self.r = radius
#         self.ingredients = ingredients

#     def cook(self):
#         print(f'готовится пицца размером {self.r * 2} cm')
    
#     @classmethod
#     def four_cheese(cls, r):
#         pizza = cls(r, 'моцарела', 'чедер', 'голландский', 'брынза')
#         return pizza


# pizza1 = Pizza(17, 'пеперони', 'моцарела', 'грибы')
# # pizza2 = Pizza(15, 'моцарела', 'чедер', 'голландский', 'брынза')
# # pizza3 = Pizza(20, 'моцарела', 'чедер', 'голландский', 'брынза')
# pizza2 = Pizza.four_cheese(15)
# pizza3 = Pizza.four_cheese(20)


# class Person:
#     surname = 'Stark'

#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age
    
#     @classmethod
#     def from_birth_date(cls, name, date_birth):
#         from datetime import date
#         age = date.today().year - date_birth
#         return cls(name, age)

# obj = Person('John', 24)
# print(obj.name, obj.surname, obj.age)
# obj2 = Person.from_birth_date('Sansa', 1999)
# print(obj2.name, obj2.surname, obj2.age)


# staticmethod - просто функции внутри классса, которые не взаимодействуют ни с классом, ни с объектом. Находятся они внутри класса лишь потому что их используют только внутри класса, так как они вне бесполезны
# @staticmethod - декоратор

# class C:
#     @staticmethod
#     def static_method():
#         print('статический метод!')

# obj = C()
# obj.static_method()
# C.static_method()

# class Cylinder:
#     def __init__(self, diameter, height) -> None:
#         self.di = diameter
#         self.h = height
#         self.area = self.get_area(self.di, self.h)

#     @staticmethod
#     def get_area(diameter, h):
#         from math import pi
#         circle = pi * (diameter / 2) ** 2
#         side = pi * h * diameter
#         area = circle * 2 + side
#         return round(area, 2)

# obj = Cylinder(10, 7)
# print(f'Area: {obj.area}')

# obj1 = Cylinder(4, 10)
# print(f'Area: {obj1.area}')
