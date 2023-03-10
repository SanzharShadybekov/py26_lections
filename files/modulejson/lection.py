# JSON - JavaScript Object Notation
# Единый формат, хранения и передачи данных между приложениями, сайтами, сервисами и языками программирования через четь интеренет.
# <filemaname>.json # файл в формате JSON

# {
#     "id": 1,
#     "author": "Ed Sheeran",
#     "title": "Perfect",
#     "year": 2015,
#     "hit": true,
#     "feat": null
# } --- Это JSON
# наша задача научиться переволить данные JSON в Python dictionary

# !!!
# JS object == {key: value}
# PY dict == {key: value}
# JSON == {key: value}

# Процессы Сериализации и Десериализации данных

# Сериализация (Запись данных в JSON) - Это перевод из Pyhhon объектов в JSON формат

# json.dump -> метод записывает Python данные в файл в формате JSON, паралленьно сделав сериализацию
# json.dumps -> метод записывает Python данные в строку в формате JSON, паралленьно сделав сериализацию

# Десериализация (Чтение данных из JSON) -> это процесс перевода из JSONa в PY dict

# json.load -> метод который считывает файл в формате JSON и переволит его в PY object
# json.loads -> метод который считывает текст в формате JSON и переводит его в PY object

# ------------------------------
# Процесс сериализации
# import json

# dict_ = {
#     'name': 'John',
#     'last_name': 'Snow',
#     'status': True,
#     'age': 24,
#     'wife': False,
#     'children': None
# }
# print(dict_)
# print(type(dict_))

# json_text = json.dumps(dict_)
# print('-------------')
# print(json_text)
# print(type(json_text))

# -------------------------------
# import json

# dict_ = {
#     'name': 'John',
#     'last_name': 'Snow',
#     'status': True,
#     'age': 24,
#     'wife': False,
#     'children': None
# }
# print(dict_)
# print()

# with open('new.json', 'w') as file:
#     json.dump(dict_, file)

# with open('new.json', 'r') as file:
#     data = file.read()
#     print(data)

# ----------------------------
# процесс десериализации
# import json

# with open('new.json', 'r') as file:
#     json_data = file.read()

# print(json_data)
# print(type(json_data))

# dict_ = json.loads(json_data)
# print(dict_, type(dict_))

# import json

# with open('new.json') as file:
#     dict_ = json.load(file)
#     print(dict_)
#     print(type(dict_)) 

# -------------------------
# https://34.12.121.10/users/ -> запрос на получение всех юзеров

from urllib.request import urlopen
import json

url = 'https://randomuser.me/api/'
json_data = urlopen(url)

print(json_data)
# print(dir(json_data))
# print(json_data.read())

dict_ = json.load(json_data) # .loads(json_data.read())
print(dict_)
print(type(dict_))



































