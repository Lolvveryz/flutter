import telebot, time
from telebot import types
from person import Person
import data
players = {}
bot = telebot.TeleBot("6159454834:AAEg-kIcwp5JA8_QOGVPXibuo14YCj4rs5I")

    
def set_m(bot, mess):
    bot.delete_message(mess.chat.id, data.mes)
    bot.delete_message(mess.chat.id, data.mes-1)
    bot.delete_message(mess.chat.id, mess.id)
    data.mes = 0
    data.text = "Зареєстровані :\n"


def group(mess):
    
    if mess.text == "/bunker" or mess.text == "/bunker@shuuurick_bot":
        if not players:
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Реєстрація", callback_data="reg"))
            players[0]=0
            bot.send_message(mess.chat.id, "Реєстрація", reply_markup=markup)
        else:
            bot.delete_message(mess.chat.id, mess.id)


    elif mess.text == "/users" or mess.text == "/users@shuuurick_bot":
        bot.send_message(mess.chat.id, players)

    elif mess.text == "/start" or mess.text == "/start@shuuurick_bot":
        set_m(bot, mess)

        if len(players) > 0:
            bot.send_message(mess.chat.id, "Початок гри")
            for _id,n in players.items():
                if _id:
                    players[_id] = Person(_id, (f"@{mess.from_user.username}") if mess.from_user.username != None else mess.from_user.first_name)
                    user = players[_id].get()
                    text = f'{user["username"]}\n\nПрофесія💼 - {user["profession"]}\nСтать та вік👤 - {user["biology"]}\nХобі🎮 - {user["hobi"]}\nБагаж📦 - {user["bagazh"]}\nЗдоров\'я🩻 - {user["heal"]}\nФакти📌 - {user["fakti"]}\nОсобливі умови‼️ - {user["bunker"]}'
                    bot.send_message(_id, text)
                    print()

        else :
            bot.send_message(mess.chat.id, "Замало гравців")
            players.clear

