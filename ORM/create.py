import peewee
from models import Category, Product
import random


def add_category(name):
    try:
        data = Category(name=name.lower().strip())
        data.save()
        print(f'Сохранили категорию {name.strip()}!')
    except (peewee.IntegrityError, peewee.InternalError):
        print('Такая категория уже существует!')

# add_category('  платья    ')
# add_category('Джинсы')
# add_category('Футболки')
# add_category('Свитеры')
# add_category('Обувь')

def add_product(name, price, category_name):
    try:
        category_id = Category.get(name=category_name.lower().strip())
    except peewee.DoesNotExist:
        category_id = None

    if category_id:
        data = Product(title=name, price=price, category_id=category_id)
        data.save()
        print(f'Сохранили товар {name}!')
    else:
        print(f'Категории {category_name} не существует!')

# add_product('Zara t-shirt', 300, 'футболки')
# add_product('Supreme t-shirt', 200, 'Футболки')
# add_product('DG t-shirt', 1000, 'Футболки')
# add_product('Aygen 48', 1500, 'Платья')
# add_product('Platye 50', 400, 'Платья')
# add_product('Lewys 1110', 2000, 'Джинсы')
# add_product('Nike Air Jordan', 4000, 'обувь')
# add_product('Badlon12', 800, 'свитеры')


# ---------------
# добавление новых данных

# add_category('cars')
# add_category('telefony')

# with open('files/cars.txt', 'r') as file:
#     ls = file.readlines()
#     # print(ls)
#     for x in ls:
#         name = x.replace('\n', '')
#         price = random.randint(5000, 200000)
#         add_product(name, price, 'cars')

# with open('files/telefon.txt', 'r') as file:
#     ls = file.readlines()
#     for x in ls:
#         name = x.replace('\n', '')
#         price = random.randint(200, 1000)
#         add_product(name, price, 'telefony')

