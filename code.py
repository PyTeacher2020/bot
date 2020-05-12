import telebot

bot = telebot.TeleBot('1163060645:AAFJCM4Ud8ytSwYAjQVi4TS8Oi04hBMbxp4')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

bot.polling()