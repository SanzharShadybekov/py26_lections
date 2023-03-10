from models import Product, Category


# Обновление данных
# query = Product.update(price=500).where(Product.title == 'Zara t-shirt')
# print(query)
# query.execute()

# query = Product.update(price=(Product.price + Product.price * 0.5)) #увеличиваем все товарам цену
# query.execute()

# query = Product.update(price=3).where(Product.category_id == 1 and Product.category_id == 8)
# query.execute()

# Удаление данных
# удаление через запрос
# query = Product.delete().where(Product.id == 16)
# query.execute()

# удаление через объект
# product = Product.get(id=14)
# print(product, product.title)
# product.delete_instance()

# query = Product.delete().where(Product.id >= 9)
# print(query)
# query.execute()

