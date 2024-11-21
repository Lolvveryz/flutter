import telebot
bot = telebot.TeleBot("6159454834:AAEg-kIcwp5JA8_QOGVPXibuo14YCj4rs5I")

def private(mess):
    bot.send_message(mess.chat.id, "пріват")


