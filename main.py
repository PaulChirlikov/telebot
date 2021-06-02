import telebot
import random

bot = telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Hello!")
@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == 'Рандомное число':
        bot.send_message(message.chat.id, str(random.randint(0, 100)))
    elif message.text == 'Как дела?':
        bot.send_message(message.chat.id, 'Отлично, сам как?')
    else:
        bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')

bot.polling()


