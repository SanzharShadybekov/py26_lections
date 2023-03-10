import json
import telebot
from telebot import types
from parse import parse_news

token = '6147778753:AAHKHXdW_f2fTmrDfB35NzLpVlkJ37he1BI'

bot = telebot.TeleBot(token)

keyboard = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('Фото')
button2 = types.KeyboardButton('Описание')
keyboard.add(button1, button2)

def read_news():
    with open('data.json') as file:
        data = json.load(file)
    return data

@bot.message_handler(commands=['start'])
def start_parse(message):
    print('!!!!!!!!!!!!!!!!!!!!!!')
    bot.send_message(message.chat.id, 'Бот приветсвует вас, мы начали парсинг!\nПодождите пару секунд...')
    print('started')
    parse_news()
    print('parsed')
    data = read_news()
    for x in data:
        print(x)
        bot.send_message(message.chat.id, f'{x} --> *{data[x]["title"]}*', parse_mode='Markdown')
    
    message_from_bot = bot.send_message(message.chat.id, 'Выберите число новости для подробной инфоормации(1-20): ')
    bot.register_next_step_handler(message_from_bot, check_number)

def check_number(message):
    keys = [str(x) for x in range(1, 21)]
    if message.text not in keys:
        print(message.text)
        message_from_bot = bot.send_message(message.chat.id, 'Неверное число нужно выбрать число  в диапазоне от (1-20): ')
        bot.register_next_step_handler(message_from_bot, check_number)
    else:
        data = read_news()
        message_from_bot = bot.send_message(message.chat.id,
                                            f'{data[message.text]["title"]}\nВыберите фото или описание этой новости!', reply_markup=keyboard)
        bot.register_next_step_handler(message_from_bot, show_info, message.text, data)

def show_info(message, number, data):
    if message.text == 'Фото':
        bot.send_message(message.chat.id, data[number]['img'])
        message_from_bot = bot.send_message(message.chat.id, 'Выберите число новости для подробной инфоормации(1-20): ')
        bot.register_next_step_handler(message_from_bot, check_number)
    else:
        bot.send_message(message.chat.id, data[number]['desc'])
        message_from_bot = bot.send_message(message.chat.id, 'Выберите число новости для подробной инфоормации(1-20): ')
        bot.register_next_step_handler(message_from_bot, check_number)

bot.polling()


