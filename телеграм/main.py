import telebot

token = '5886592720:AAGsMJgoWTs6rZhEPAmpQLZtWG1tqOfXbv4'
Bot = telebot.TeleBot(token)


@Bot.message_handler(func=lambda m: True)
def get_text_messages(message):
  if message.text == "Привет" or message.text == '/start':
      Bot.reply_to(message, "Привет, сейчас я твой консультант.")
  elif message.text == "/help":
      Bot.reply_to(message, "Напиши Привет")
  else:
      Bot.reply_to(message, "Я тебя не понимаю. Напиши /help.")
Bot.infinity_polling()