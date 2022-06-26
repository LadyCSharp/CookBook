import telebot
from telebot import apihelper
import time
import os
import requests
import random
import urllib
# TOKEN='5203104381:AAHmxnTLcCpMc9LlACMfwJW6CUEAheEssKs'
TOKEN='5410019879:AAGjU-c-hHZo3ynf74ljEyVnFoY7OpZ3guk'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Ты готов готовить?")
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
def category_list(message):
    # получить то что после команды
    mess=""
    token = '99ab153ad4d73141ab117ba94b3bef8179a87d62'
    headers = {'Authorization': f'Token {token}'}
    #rooturl = 'http://127.0.0.1:8000'
    rooturl = '194.87.92.56'
    # url=os.path.join(rooturl,'/api/v0/categories/')
    url ='https://' + rooturl+ ':8080/api/v0/categories/'
    print(url)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        for item in response.json():
            mess += item['name']+"\n"
    else:
        mess='что-то пошло не так'

    bot.reply_to(message, mess)

@bot.message_handler(commands=['rnd'])
def rnd(message):
    # получить то что после команды
    mess=""
    token = '99ab153ad4d73141ab117ba94b3bef8179a87d62'
    headers = {'Authorization': f'Token {token}'}
    #rooturl = 'http://127.0.0.1:8000'
    rooturl = '194.87.92.56'
    # url=os.path.join(rooturl,'/api/v0/categories/')
    url ='https://' + rooturl + ':8080/api/v0/recipe1/'
    print(url)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        item = random.choice(response.json())
        if item['hi']:
            # bot.send_message(message.chat.id, item['picture'])
            # photo = open(item['picture'], 'rb')
            f = open('out.jpg', 'wb')
            f.write(urllib.request.urlopen(item['picture']).read())
            f.close()
            img = open('out.jpg', 'rb')
            bot.send_photo(message.chat.id, img)


        # print( type(item['sostav']))
        sos = item['sostav'].replace(',',"\n-").replace('Ingredient_Recipe:', "").replace('<',"").replace('>',"").replace('[',"-").replace(']',"")

        mess = item['name']+"\n"+sos+"\n"+item['text']+"\n"
        # mess = item['name'] + "\n" + item['text'] + "\n" + ' '.join(item['ingredients'])
    else:
        mess='что-то пошло не так'

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