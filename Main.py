import telebot

bot = telebot.TeleBot("486413931:AAF-xIPU2vPB8zIslULHuDd1VIXzVMMHo6k")

upd = bot.get_updates()

last_upd = upd[-1]

message_from_user = last_upd.message

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('Спросить дз')
    
    bot.send_message(message.from_user.id, "Привет! Я - бот, отправляющий домашнее задание на следующий день для школьников 627 школы 10Б класса", reply_markup=user_markup)

@bot.message_handler(commands=['help'])
def handle_text(message):
    answer = "Чтобы спросить у меня о домашнем задании нажмите на команду Ask"
    bot.send_message(message.chat.id, answer )




@bot.message_handler(content_types=['text'])
def handle_text(message):
    answer = "Нажимайте на кнопку!"
    bot.send_message(message.chat.id, answer)

@bot.message_handler(content_types=['Спросить дз'])
def handle_text(message):
    answer = "К сожалению, домашнее задание на завтра пока не выложено. Напишите мне немного позже!"
    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True, interval=0)

