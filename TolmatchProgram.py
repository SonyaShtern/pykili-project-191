import telebot, eng_rus, rus_eng, adding_word
from telebot import apihelper, types


apihelper.proxy = {"https": "socks5://user42399:zeno9h@45.90.197.187:18943",
                   "https": "socks5://127.0.0.1:9050"}

bot = telebot.TeleBot('1141035100:AAFo_9NZP2md2XjIpUrZWalV7cmeYee4v0A')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     'Привет, это бот Толмач!'
                     '\nМожет быть, он будет тебе полезен.'
                     '\n/perevod - переведет слово'
                     '\n/help - расскажет, как собой пользоваться')


@bot.message_handler(commands=['perevod'])
def ask_language(message):
    keyboard = types.InlineKeyboardMarkup()
    key_rus_eng = types.InlineKeyboardButton(text='rus->eng', callback_data='rus->eng')
    key_eng_rus = types.InlineKeyboardButton(text='eng->rus', callback_data='eng->rus')
    keyboard.row(key_eng_rus, key_rus_eng)
    question = 'С какого языка на какой хотите переводить?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def perevod(call):
    if call.data == 'rus->eng':
        bot.send_message(call.message.chat.id, 'Чтобы остановиться наберите \"stop\".')
        bot.send_message(call.message.chat.id, 'Что вы хотите перевести?')
        bot.register_next_step_handler(call.message, ruseng)
    elif call.data == 'eng->rus':
        bot.send_message(call.message.chat.id, 'Чтобы остановиться наберите \"стоп\".')
        bot.send_message(call.message.chat.id, 'Что вы хотите перевести?')
        bot.register_next_step_handler(call.message, engrus)

def engrus(message):
    zapros = message.text.lower()
    if zapros == "стоп":
        bot.send_message(message.chat.id, "Ok)")
    else:
        bot.send_message(message.chat.id, eng_rus.main(zapros))
        bot.send_message(message.chat.id, 'Что вы хотите перевести?')
        bot.register_next_step_handler(message, engrus)

def ruseng(message):
    zapros = message.text.lower()
    if zapros == "stop":
        bot.send_message(message.chat.id, "Ok)")
    else:
        bot.send_message(message.chat.id, rus_eng.main(zapros))
        bot.send_message(message.chat.id, 'Что вы хотите перевести?')
        bot.register_next_step_handler(message, ruseng)

@bot.message_handler(commands=['add_slovo'])
def add_slovo(message):
    bot.send_message(message.chat.id, 'Введите слово с его переводом в следующем формате:'
                                      '\nСлово на английском, символ \';\', перевод на русский. Без пробелов и прочих символов.'
                                      '\nWord;перевод'
                                      '\n\nЧто вы хотите добавить? ')
    bot.register_next_step_handler(message, adding)

def adding(message):
    new_slovo = message.text.lower()
    bot.send_message(message.chat.id, adding_word.adding(new_slovo)) # еще не написано

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,
                     'Этот бот способен переводить какое-то количесво слов с английского и'
                     ' давать к ним толкования, если слова не совсем простые. '
                     '\nПопросить бота что-то перевести можно через команду /perevod. '
                     '\nПостарайтесь вводить слова без опечаток и ошибок, иначе Толмач не справится.'
                     '\nЕсли в ответ на ваш запрос пришло такое сообщение: --, значит Толмач не знает слова или его толкования.'
                     '\nВ этом случае вы можете воспользоваться командой /add_slovo и пополнить словарный запас Толмача.')


bot.polling(none_stop=True)
