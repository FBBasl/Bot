import telebot

bot = telebot.TeleBot("486413931:AAF-xIPU2vPB8zIslULHuDd1VIXzVMMHo6k")

upd = bot.get_updates()

last_upd = upd[-1]

message_from_user = last_upd.message

@bot.message_handler(commands=['help'])
def handle_text(message):
    answer = "Мои возможности ограничены. Sorry!"
    bot.send_message(message.chat.id, answer )

@bot.message_handler(commands=['start'])
def handle_text(message):
    answer = "Hello! You are welcome!"
    bot.send_message(message.chat.id, answer)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    answer = "Cегодня понедельник, дз пока не задали. Позже вечером, на сервер придет информация об дз!"
    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True, interval=0)

