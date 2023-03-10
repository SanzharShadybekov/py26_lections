# Ассоцицая - означает что внутри одного объекта будет существовать другой объект в качестве аттрибута
# 1. Композиция - сильная связь
# 2. Агрегация - слабая свзязь


# Композиция - это когда стена не существует одельно от комнаты. Она создается при создании комнаты и полностью управляется классом комнаты

# class Wall:
#     def __init__(self, direction) -> None:
#         self.type = direction

#     def __str__(self) -> str:
#         return f'{self.type} wall!'

#     def info(self):
#         print('White wall')

# class Room:
#     def __init__(self) -> None:
#         self.west_wall = Wall('west')
#         self.east_wall = Wall('east')
#         self.south_wall = Wall('south')
#         self.north_wall = Wall('north')

# room = Room()
# print(room.west_wall)
# print(room.north_wall)
# print(room.north_wall.type)
# room.north_wall.info()


# Агрегация - это когда экземпляр двигателя создается где то в другом месте, и передается в класс Авто в качестве параметре 

# class Engine:
#     country = 'Germany'
#     def __init__(self, power) -> None:
#         self.power = power

#     def __str__(self) -> str:
#         return f'Engine: {self.power}'

# class Car:
#     model = 'Audi'
#     country = 'Germany'

#     def __init__(self, type, engine) -> None:
#         self.type = type
#         self.engine = engine
    
#     def __str__(self) -> str:
#         return f'{self.model} {self.type} -> {self.engine} {self.engine.country}'
    
# engine = Engine(500)
# car = Car('A8', engine)
# print(car)

# ----------------------

# class Battery:
#     _power = 100

#     def power(self):
#         if self._power < 100:
#             self._power = 100

# class Iphone:
#     def __init__(self, color) -> None:
#         self.color = color
#         self.battery = Battery()
#         # когда мы создаем объект внутри - композиция

# class Nokia:
#     def __init__(self, color: str, battery: Battery):
#         self.color = color
#         self.battery = battery
#         # когда принимаем в качестве параметра - агрегация

# iphone = Iphone('Gray')
# iphone2 = Iphone('Silver')
# del iphone
# # при удалении iphone вместе с ним удаляется и battery

# battery = Battery()
# nokia = Nokia('black', battery)
# del nokia
# # при удалении нокии батарейка остается
# nokia2 = Nokia('white', battery)




