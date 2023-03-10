# PostgreSQL - Система управления базами данных (СУБД/DBMS)
# Это ряд программ и интсрументов позволяющих создавать БД, управлять ею и манипулировать данными внутри БД(CRUD).

# Postgres - Сама база данных, она реалиционная, то есть данные хранятся в виде таблиц и таблицы имеют связи между собой (relations).

# SQL (Structured Query Language) - декларативный язык структурированных запросов, он применяется для создания и управления данными

# -------------------------------
# Типы полей в Postgres

# 1. Numeric types:
        # a. smallint (2 bytes) -> -32767 to 32767
        # b. integer (4 bytes) -> -2147000 to 2147000
        # c. bigint(8 bytes) -> ...
        # d. serial (4 bytes) -> auto-increment(integer, 1-2147000)
        # c. real(4 bytes) - число с плавающей точкой, вещественное число
        # f. double precision (8 bytes)  - real но только с двойной точностью
# 2. Character types:
    # a. varchar(кол-во 255) - можем указать макс кол-во символов в ручную.  Если мы укзалали мак кол-во символов в 50, а заполнили только 10, то остальные 40 не заполнятся
    # b. char(255)- если не заполним все символы то остальные заполняться пробелами
    # с. text - неограниченное кол-во символов

# 3. Boolean types
    # boolean(1 byte) -> True/False

# 4. date - календарная дата (год.месяц.день)

# 5. location (point) - координатная точка -> (245, -12) (x, y)

# ---------------------------------
# Связи между таблицами(relations):
    # 1. Один к одному(One-to-One) - человек паспорт
    # 2.  Один ко многим(One-to-Many) - человек и банковские карты
    # 3. Много ко многим(Many-to-Many) - студенты и преподы

# constraints(Ограничения):
    # 1. CHECK <column> > 5 - проверка данных по условию
    # 2. UNIQUE - только уникальные значения
    # 3. NOT NULL - обязательно к заполнению
    # 4. DEFAULT <value> - добавляет дефолтное значение
    # 5. PRIMARY KEY (для установки идентификатора данных в таблице)
    # 6. FOREIGN KEY (для установки связи между таблицами)


# добавление к таблице которая уже есть
# ALTER TABLE cities ADD CHECK (name <> '');
# ALTER TABLE products ADD CONSTRAINT <name_of_constr> UNIQUE (name);
# ALTER TABLE cities ALTER COLUMN location SET NOT NULL;

# -------------------------------
# Вход
# ubuntu: sudo -u postgres psql
# mac: psql postgres
# psql -> для вхого через своего юзера

# \q -> выход из СУБД

# \du -> список всех юзеров

# \l -> cписок всех баз данных

# \c <dbname> -> команда для подключения к бд
        # \dt -> список таблиц в бд
        # \d <table name> -> подробная инфоомация про таблицу

# ИМПОРТ данных при помощи файла
# psql -U <username> -d <database> -f <path_to_file>

# CREATE DATABASE <dbname>; -> комнада для создания бд
# DROP ... -> удаление

# CREATE TABLE <tablename> (
    # <name_of_column> <type>,
    # <name_of_column> <type>,
# ); команда для создания таблицы 

# CREATE TABLE weather (
#     city varchar(80),
#     temp_lo int, 
#     temp_hi int,
#     prcp real,
#     date date
# );

# DROP DATABASE <name_of_db>; - удаление бд

# DROP TABLE <name_of_table>; - удаление таблицы

# INSERT INTO <tablename> (<columns>) VALUES
    # (datas_to_columns); - команда для заполнения данных в таблицу

    # INSERT INTO cities (name, location)
    # VALUES ('Bishkek', '(42.52, 74.59)')

# UPDATE <tablename> SET <row> = <new_value>
# WHERE <row> = <value>; - команда для обновления данных
# Указываем после WHERE то какой объект обновить

# DELETE FROM <tablename> WHERE <column> = <data>; - команда для удаления

# СREATE USER <username> WITH PASSWORD '<password>'; -> комнада для создания юзера

# ALTER USER <username> WITH SUPERUSER; команда для изменения статуса юзера на суперюзера 

# SELECT <column> FROM <table>; команда для получения данных

# WHERE: используется для фильрации по полям. будут выводиться только те данные которые соответсвуют условию WHERE
# Синтаксис: SELECT <row> FROM <tablename> WHERE <row> = 'чему либо'

# SELECT * FROM products WHERE meat = 'Becon';
# SELECT * FROM products WHERE meat in ('Becon', 'Beef');

# AND: оператор и, для множетсва условий

# Операторы сравнения: >, <, >=, <=, =, <>

# BETWEEN: Уcловие между
# SELECT * FROM products WHERE id BETWEEN 3 and 8;
# SELECT * FROM products WHERE id <= 8 and id >= 3;

# ORDER BY: сортировка по входящим данным по убыванию или возрастанию
        # ASC(по возрастанию) и DESC(по убыванию)
# SELECT <row> FROM <table> ORDER BY <row> [ASC/DESC];

# LIMIT: Позволяет нам вернуть данные в ограниченном кол-ве
# SELECT <row> FROM <table> LIMIT 1;

# LIKE: Выводит результат который соответсвует введеному шаблону. Зависит от регистра
# ILIKE: не зависит от регистра

# Синтаксис: SELECT * FROM products WHERE name LIKE 'S%';

# DISTINCT: Позволяет нам убрать дубликаты и возвращает только уникальные знчения
# SELECT DISTINCT name FROM products;

# GROUP BY разделяет данные которые мы получаем в SELECT, при этом группируя их по определенному признаку, и теперь для каждой группы можно использовать агрегатную функцию

# SELECT city, MAX(temp_hi), AVG(prcp) FROM weather GROUP BY city;

# HAVING: он раоботает так же как и WHERE, только с оператором GROUP BY

# -----------------------------

# JOIN - оператор, который позволяет в запросах селект брать данные из нексольких таблиц

# INNER JOIN() - достаются только те записи, у которых есть связь

# FULL JOIN - достаются все записи с обеих таблиц

# LEFT JOIN - достает все записи с левой таблиццы, а с правой только те записи у которых есть связь с левой таблицей

# RIGHT JOIN - достает все записи с правой таблиццы, а с левой только те записи у которых есть связь с правой таблицей

# * где "левая" таблица это та таблица которая записана до join, а "правая" таблица это таблица которая записаана после join

