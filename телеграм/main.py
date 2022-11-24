import telebot
from telebot import types
import data_base

Bot = telebot.TeleBot('5886592720:AAGsMJgoWTs6rZhEPAmpQLZtWG1tqOfXbv4')
user_index = 0

@Bot.message_handler(commands=['start','help'])
def login_1(m, res=True):
    Bot.reply_to(m, 'Здравствуйте, я текстовый помощник NeoBank! Введите ваш номер телефона для'
    + ' дальнейших действий')

@Bot.message_handler(func=lambda m: True)
def login_2(message):
    login_check = 0
    for i in range(len(data_base.all_users)):
        if data_base.all_users[i][2] == message.text:
            login_check += 1
            user_index = i
            Bot.reply_to(message, 'Введите cvc код для подтверждения, что вы владелец карты')
            break
    if login_check == 0:
        Bot.reply_to(message, 'Неверно введённый номер телефона')
#def login_3(message): ЗАВТРА ДОДЕЛАТЬ!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    


@Bot.message_handler(func=lambda m: True)
def functions(m, res=False):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    first_item = types.KeyboardButton('Баланс')
    second_item = types.KeyboardButton('Анализ финансов')
    third_item = types.KeyboardButton('Что-то с банком, я хз')
    markup.add(first_item)
    markup.add(second_item)
    markup.add(third_item)
    Bot.send_message(m.chat.id, 'Вы успешно вошли. Выберите, что вы хотите сделать', reply_markup=markup)

@Bot.message_handler(content_types=['text'])
def message_text(message):
    answer = ''
    if message.text.strip()=='Баланс' :
        answer = 'Ты бомж'
    elif message.text.strip()=='Анализ финансов' :
        answer = 'Тебе пора на трассу'
    elif message.text.strip()=='Что-то с банком, я хз' :
        answer = 'Я реально хз'

    Bot.send_message(message.chat.id, answer)

Bot.polling(non_stop=True, interval=0)