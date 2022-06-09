import telebot
from telebot import apihelper
import time
import os
import requests

TOKEN='5203104381:AAHmxnTLcCpMc9LlACMfwJW6CUEAheEssKs'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")
help='/timer - Таймер на 10 секунд \n/help - помощь\n/list - список категорий\n/rnd - случайный рецепт\n/echo - эхо\n/rev - перевернутое эхо'
@bot.message_handler(commands=[ 'help'])
def send_help(message):
    bot.reply_to(message, help)
# Команда в параметром
@bot.message_handler(commands=['say'])
def say(message):
    # получить то что после команды
    text = ' '.join(message.text.split(' ')[1:])
    bot.reply_to(message, f'***{text.upper()}!***')


@bot.message_handler(commands=['rev'])
def rev(message):
    # получить то что после команды
    text = ' '.join(message.text.split(' ')[1:])
    bot.reply_to(message, text[-1::-1])


@bot.message_handler(commands=['echo'])
def echo(message):
    # получить то что после команды

    bot.reply_to(message, ' '.join(message.text.split(' ')[1:]))

@bot.message_handler(commands=['list'])
def list(message):
    # получить то что после команды
    mess=""
    token = '99ab153ad4d73141ab117ba94b3bef8179a87d62'
    headers = {'Authorization': f'Token {token}'}
    response = requests.get('http://127.0.0.1:8000/api/v0/categories/', headers=headers)
    for item in response.json():
        mess += item['name']+"\n"

    bot.reply_to(message, mess)


# Обработка команд
@bot.message_handler(commands=['timer'])
def timer(message):
    for i in range(10):
        time.sleep(1)
        bot.send_message(message.chat.id, i + 1)

@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    FILE_ID = 'CAADAgADPQMAAsSraAsqUO_V6idDdBYE'
    bot.send_sticker(message.chat.id, FILE_ID)


bot.polling()