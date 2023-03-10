# ООП - Объектно-ориентированное программирование

# Класс ->  это описание того, как должен выглядеть объект, то есть в классе мы описывае какими свойствами(данными) и поведением(фукнциями) должен обладать объект

# Объект -> это сущность которую мы создаем от класса, у объекта есть состояние свойств(данных)

# Целью создание было связать данные(аттрибуты) с функциями(методы) которые использовали их

# Свойствами(аттрибуты) - называют обычные переменные внутри класса, в которых хранятся данные определенного объекта

# Методы - это обычные функции которые описывают поведение объекта, фукнции внутри класса называют методами

# ------------------------------

# john = ['John', 'Snow', 'King of North', 5000, 30]

# def show_info(human):
#     print(f'Name: {human[0]} {human[1]}, Age: {human[-1]}, Job: {human[2]}, Salary: {human[3]}')

# # show_info(john)


# class Human:
#     def __init__(self, name, last_name, age, job, salary):
#         self.name = name + " " + last_name
#         self.age = age
#         self.job = job
#         self.salary = salary

#     def show_info(self):
#         return f'Name: {self.name}, Age: {self.age}, Job: {self.job}, Salary: {self.salary}'

# john = Human('John', 'Snow', 30, 'King of North', 5000)
# sultan = Human('Sultan', 'Katana', 19, 'Mentor', 100)

# # print(dir(john))
# print(john.show_info())
# print(john.name)
# print(john.age)
# print('----------')
# print(sultan.show_info())
# print(sultan.name)

# ------------------------------

# class Dog:
#     # аттрибуты класса
#     age = 0
#     ushi = True

#     def __init__(self, name, color):
#         """Инициализатор, именно здесь создаются аттриьуты объекта"""
#         # в self прилетает ссылка на объект от класса
#         self.name = name  # аттрибуты объекта
#         self.color = color

#     def bark(self):
#         print(f'{self.name} лает!')

# bobik = Dog('Bobik', 'brown')
# yumi = Dog(name='Yumi', color='white')
# aktosh = Dog('Aktosh', 'gray')

# print(f'name: {bobik.name}, age: {bobik.age}, color: {bobik.color}, ushi: {bobik.ushi}')
# print(f'name: {yumi.name}, age: {yumi.age}, color: {yumi.color}, ushi: {yumi.ushi}')
# print(f'name: {aktosh.name}, age: {aktosh.age}, color: {aktosh.color}, ushi: {aktosh.ushi}')

# bobik.age = 2
# yumi.age = 1
# aktosh.age = 3
# aktosh.ushi = False

# print('After')
# print(f'name: {bobik.name}, age: {bobik.age}, color: {bobik.color}, ushi: {bobik.ushi}')
# print(f'name: {yumi.name}, age: {yumi.age}, color: {yumi.color}, ushi: {yumi.ushi}')
# print(f'name: {aktosh.name}, age: {aktosh.age}, color: {aktosh.color}, ushi: {aktosh.ushi}')

# yumi.bark()

# ------------------------------

# class Human:
#     def __init__(self):
#         print('init worked')
#         self.golod = 100
#         self.raychel = 'raychel'
    
#     def eat(self, meal, doel=True):
#         if doel:
#             self.golod -= 50
#         else:
#             self.golod -= 25

    
# obj = Human()
# print(dir(obj))
# print(obj.golod)
# obj.name = 5
# obj.eat('burger', doel=False)
# print(obj.golod)
# print(obj.name)
# print(dir(obj))



