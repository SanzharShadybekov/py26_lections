# Mixins
# Миксины - классы, которые будут использоваться для наследования, но от этих миксинов не создают объекты
# Для чего:
# 1. вы хотите предоставить множество доп методов для класса
# 2. вы хотите использовать одну конкретную фукнцию во множестве разных классов

# class Machines:
#     def start_engine(self):
#         print('started engine!')

# class RadioMixin:
#     def play_radio(self):
#         print('music is playing')

# class Auto(RadioMixin, Machines):
#     pass

# class Plane(Machines):
#     pass

# class Train(RadioMixin, Machines):
#     pass

# obj = Auto()
# obj2 = Plane()
# obj3 = Train()

# obj.start_engine()
# obj2.start_engine()
# obj3.start_engine()

# obj.play_radio()
# obj3.play_radio()


class FlyMixin:
    @staticmethod
    def fly():
        print('я могу летать')

class WalkMixin:
    @staticmethod
    def walk():
        print('я могу ходить')

class SwimMixin:
    @staticmethod
    def swim():
        print('я могу плыть')

class Human(WalkMixin, SwimMixin):
    name = 'человек'

    def talk():
        print('я могу говорить')

class Fish(SwimMixin):
    name = 'рыба'

class Exocoetidae(SwimMixin, FlyMixin):
    name = 'летучая рыба'

class Duck(SwimMixin, WalkMixin, FlyMixin):
    name = 'утка'

obj = Human()
obj.walk()
obj.talk()