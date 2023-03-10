# Работа с файлами

# Каретка - Указатель - Курсор

# open(<путь до файла>)

# file = open('/home/sanzhar/Desctop/py.26/files/files.py') # Абсолютный путь

# file = open('files.py') # Относительный путь
# ~ working -> Desctop/py.26/files/files.py
# py.26 -> files/files.py

# file = open('files.py')
# data = file.read()
# print(type(data))
# file.close()

# Режимы работы с файлами
# 1 . r/r+ (read)
# 2.  w/w+ (write)
# 3   a/a+ (append)
# b, x


# file = open('test.txt', 'r')
# print(file.read())
# file.close()

# file = open('test.txt', 'r')
# data = file.readlines()
# print(data)
# print(len(data[0]))
# file.close()

# file = open('test.txt', 'r')
# print(file.readline())
# print('!!!!')
# print(file.read())
# file.close()


# контекстный менеджер
# with open('test.txt', 'r') as file: # file = open('test.txt')
#     data = file.read()
#     print(data)
#     print(file, 'inside')

# print(file.read(), 'outside')


# with open('test.txt', 'r') as f:
#     print(f.tell())
#     data = f.read(20)
#     print(f.tell())
#     print(data)
#     print(f.read())
#     print(f.tell())

# file.tell() -> возвращает индекс где находиться указатель(курсор)
# file.seek(index) -> перемещает курсор на индекс который вы передали

# with open('test.txt', 'r') as file:
    # print(file.readline())
    # file.seek(0)
    # print(file.readline())
    # file.seek(0)
    # a = file.read()
    # print(file.readline())
    # print(file.readlines(-1))

# print(a)

# with open('test.txt', 'w') as file:
    # file.write('Pervaya strochka!')
    # file.write('\nHe is bastard of Ned Stark!\n')
    # file.write('This is lesson about files!')
    # file.seek(0)
    # data = ['Pervaya strochka!\n', 'He is bastard of Ned Stark!\n', 'This is lesson about files!']
    # file.writelines(data)

# with open('test.txt', 'a+') as file:
#     file.write('\nJohn Snow is North King!')
#     file.write('\nYou know nothing John Snow!')
#     file.seek(0)
#     print(file.read())

# ----------------------------------------------------

# try:
#     from PIL import Image
# except ImportError:
#     import Image
# import pytesseract
# import re

# def get_imei_code(image):
#     string = pytesseract.image_to_string(image)
#     # print(string)
#     # print(type(string))
#     list_of_imei = re.findall(r'IMEI\d.\s\d+', string)
#     print(list_of_imei)

#     with open('imei_codes.txt', 'w') as file:
#         file.writelines(f'{x}\n' for x in list_of_imei)

#         # for x in list_of_imei:
#         #     file.write(f'{x}\n')

# image = 'imei.jpg'
# get_imei_code(image)























