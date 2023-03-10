import telebot 

token = '6147778753:AAHKHXdW_f2fTmrDfB35NzLpVlkJ37he1BI'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    with open('user_file.txt', 'a') as f:
        for id_user in open('user_file.txt'):
            bot.send_message(id_user.replace('\n',''), 'выходим на перерыв, приятного аппетита')



bot.polling()