# Магические методы (dunder - double umderscore) - методы, у которых два нижних подчеркивания в начале и в конце. Магия в том, что мы их не вызываем напрямую, а они вызываются в определенный момент, либо они вызываются определенными операторами или функциями.

# res = 5 + 5 # __add__
# print(res)

# class A(int):
#     pass

# obj = A()
# print(dir(obj))

# магические методы которые срабатывают при помощи оператора:

# __eq__(self, other) -> ==  :  5 == 7  self: 5 other: 7
# __ne__(self, other) -> !=
# __lt__(self, other) -> < ;    __le__  -> <=
# __gt__(self, other) -> > ;       __ge__ -> >=

# __sub__(self, other) -> -     __div__ -> /
# __mul__ -> *    __mod__ -> %
# __floordiv__ -> //   __add__ -> +
# __pow__ -> **

# class MyClass:
#     def __init__(self, string) -> None:
#         self.string = string
    
#     def __add__(self, other):
#         print('add сработал')
#         print(self, '!!!!')
#         print(other, '****')
#         res = self.string + other.string
#         return MyClass(res)
    
#     def __str__(self) -> str:
#         return self.string

# obj1 = MyClass('John')
# obj2 = MyClass('Jamie')
# obj3 = MyClass('Lanister')
# res = obj1 + obj2 + obj3
# print(res)
# print(res.string)


# class Word(str):
#     def __init__(self, word) -> None:
#         self.word = word

#     def __gt__(self, other: str) -> bool:
#         print('gt сработал')
#         print(self, '!!!!')
#         print(other, '****')
#         return len(self) > len(other)

# obj1 = Word('John            ')
# obj2 = Word('Hello world!')
# print(obj1 > obj2)

# -----------------------
# конструктор -> __new__(cls)
# инициализатор -> __init__(self)
# вызываются, когда создаем обьект

# class Conventer(float):
#     def __new__(cls, __x):
#         print('new сработал')
#         print(cls, '!!!')
#         print(__x, 'xxx')
#         if __x < 50:
#             raise ValueError('x меньше 50!')
#         return super().__new__(cls, __x)

#     def __init__(self, x) -> None:
#         print('init сработал')
#         print(self, '!!!!!')
#         self.number = x

# obj = Conventer(65)
# print(obj)


# class Word(str):
#     def __new__(cls, word):
#         word = word.replace(' ', '')
#         return super().__new__(cls, word)

#     def __init__(self, word) -> None:
#         self.word = word

#     def __gt__(self, other: str) -> bool:
#         print('gt сработал')
#         print(self, '!!!!')
#         print(other, '****')
#         return len(self) > len(other)
    
#     def gt(self, other: str) -> bool:
#         print('custom gt сработал')
#         print(self, '!!!!')
#         print(other, '****')
#         return len(self) > len(other)

# obj1 = Word('   Jo   hn            ')
# obj2 = Word('Hello world!')
# print(obj1 > obj2) 
# print(obj1.gt(obj2))

# ---------------------
# дандер методы строкового отображения олбъектов
# __str__ -> для отображения строки, которую будут видеть пользователи
# __repr__ -> строковуб информацию о том как создать объект
# __len__  --> len(obj)
# __repr__  --> repr(obj)

# eval('6 + 6') -> 6 + 6

# class Base:
#     def __init__(self, string) -> None:
#         self.string = string

#     def __str__(self) -> str:
#         return f'Объект: {self.string}'
    
#     def __repr__(self) -> str:
#         return f'Base("string")'
    
#     def __len__(self):
#         return 5

# user = Base('Hello John')
# print(user)
# print(repr(user))
# obj1 = eval(repr(user)) # Base('string')
#             #'Base("string")'
# obj1 = Base('string')
# print(obj1)

# -------------------------------

# class Person:
#     def __init__(self, attrs: dict) -> None:
#         # self.name = attrs['name']
#         # self.a = 5 == setattr(self, 'a', 5)
#         for key, value in attrs.items():
#             setattr(self, key, value)


# alice = Person({'name': 'Alice Rose', 'income': 180000, 'eyes': 'browm'})
# john = Person({'email': 'JohnSnow@gmail.com', 'last_name': 'Snow'})
# print(f'{alice.name} -- {alice.income} -- {alice.eyes}')
# print(f'{john.email} -- {john.last_name}')

# ----------------------

# class MyList(list):
#     def __init__(self, ls):
#         self.ls = ls

#     def __getitem__(self, index):
#         print(self.ls[index - 1])

# x = MyList(['123', 'Hello', 2, 4, 5])
# x[1]
# x[3]
# x[2]

# __iter__ - вызывается, когда мы итерируем объект

# class A:
#     def __init__(self, word) -> None:
#         self.word = word

#     def __iter__(self):
#         for i in self.word:
#             print('iter method')
#             yield i

# x = A('Human')
# for i in x:
#     print(i)

# a = range(10)
# print(a)
# for x in a:
#     print(x)

# def generator(num):
#     for i in range(num):
#         yield i

# a = generator(5)
# for x in a:
#     print(x)

# ----------------------

# class User:
#     def __init__(self, name) -> None:
#         self.name = name

#     def __call__(self, name, reverse=None):
#         if reverse:
#             print(f'User object: {self.name} {name}'[::-1])
#             return
#         print(f'User object: {self.name} {name}')

# user1 = User('John Snow')
# user1("Jamie")





