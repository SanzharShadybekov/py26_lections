# Множественное наследование - это когда класс наследуется от двух или более классов


# class Auto:
#     def play_music_at_station(self):
#         print('Music is playing!')

#     def ride(self):
#         print('We\'re riding on the ground!')

# class Plane:
#     def play_music_at_station(self):
#         print('Listening Ed Sheeran!')
    
#     def fly(self):
#         print('We\'re flying!')

# class FutureAuto(Auto, Plane):
#     pass

# obj = FutureAuto()
# obj.ride()
# obj.fly()
# obj.play_music_at_station()


# class A:
#     def print_A(self):
#         print('A')

# class B:
#     def print_B(self):
#         print('B')

# class C:
#     def print_C(self):
#         print('C')


# class MyClass(A, B, C):
#     pass

# obj = MyClass()
# obj.print_A()
# obj.print_B()
# obj.print_C()
# print(MyClass.mro())

# class Test:
#     pass

# a = Test()
# print(Test.mro())
# print(dir(a))

# print(dir(object))
# Проблема ромба(решенна с помощью mro)
# MRO (Method Resolution Order) - механизм для корректного поиска родительских методов. Был создан для решения проблемы ромба, которая появилась после введения класса object в пайтон. Поиск идет таким образом что если у родительских классов один общий предок, то идет поиск в ширину.

# class Zero:
#     def say(self):
#         print('class Zero!')

# class First(Zero):
#     # def say(self):
#     #     print('class First')
#     pass

# class Second(Zero):
#     pass
#     # def say(self):
#     #     print('class Second')

# class MyClass(First, Second):
#     def say(self):
#         super().say()
#         print('My CLass')

# obj = MyClass()
# obj.say()
# print(MyClass.mro())

# проблема перекрестного наследования

# class Y:
#     pass

# class X:
#     pass

# class A(X, Y):
#     pass

# class B(Y, X):
#     pass

# class MyMRO(type):
#     def mro(cls) -> list[type]:
#         return [A, object, B, X, Y, cls]

# class MyClass(A, B, metaclass=MyMRO):
#     pass

# obj = MyClass()
# print(MyClass.mro())





