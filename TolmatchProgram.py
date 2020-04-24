import telebot, csv, codecs, programma
from telebot import apihelper, types


apihelper.proxy = {"https": "socks5://127.0.0.1:9050",
                   "https": "socks5://user42399:zeno9h@45.90.197.187:18943"}
bot = telebot.TeleBot('1141035100:AAFo_9NZP2md2XjIpUrZWalV7cmeYee4v0A')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     'Привет, это бот Толмач!'
                     '\nМожет быть он будет тебе полезен.'
                     '\n/perevod - переведет слово'
                     '\n/help - расскажет, как собой пользоваться')


@bot.message_handler(commands=['perevod'])
def doverep(message):
    bot.send_message(message.chat.id, 'Что вы хотите перевести?')
    bot.register_next_step_handler(message, perevod)

def perevod(message):
    zapros = message.text.lower()
    bot.send_message(message.chat.id, programma.main(zapros))

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,
                     'Этот бот способен переводить какое-то количесво слов с английского и'
                     ' давать к ним толкования, если слова не совсем простые. '
                     '\nПопросить бота что-то перевести можно через команду /perevod. '
                     '\nПостарайтесь вводить слова без опечаток и ошибок, иначе Толмач не справится.'
                     '\nЕсли в ответ на ваш запрос пришло такое сообщение: --, значит Толмач не знает слова или его толкования.')


bot.polling(none_stop=True)
