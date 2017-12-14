import telebot

bot = telebot.TeleBot("486413931:AAF-xIPU2vPB8zIslULHuDd1VIXzVMMHo6k")

upd = bot.get_updates()

last_upd = upd[-1]

message_from_user = last_upd.message

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('Спросить дз на завтра')
    user_markup.row('Узнать расписание на завтра📰')
    bot.send_message(message.from_user.id, "Привет! Я - школьный бот, предоставляющий информацию школьникам о дз и о расписании", reply_markup=user_markup)


@bot.message_handler(commands=['stop'])
def handle_start(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Спросить дз на завтра":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('1.Алгебра', '2.Геометрия', '3.Физика')
        user_markup.row('4.Английский язык', '5.Проект', '6.История')
        user_markup.row('7.Проект')
        user_markup.row('Вернуться назад')

        bot.send_message(message.from_user.id,"Выберите урок", reply_markup=user_markup)

    if message.text == 'Узнать расписание на завтра📰':
        answer = "1.08:30 - Алгебра \n2.09:25 - Геометрия \n3.10:30 - Физика \n4.11:35 - Английский язык \n5.12:30 - Проект \n6.13:25 - История \n7.14:30 - Проект"
        bot.send_message(message.chat.id, answer)
    if message.text == 'Вернуться назад':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Спросить дз на завтра')
        user_markup.row('Узнать расписание на завтра📰')
        bot.send_message(message.from_user.id,
                         "Что будем делать дальше?",
                         reply_markup=user_markup)

    if message.text == '1.Алгебра':
        bot.send_message(message.chat.id, '№4.35, №4.36, №4.37.')
    if message.text == '2.Геометрия':
        bot.send_message(message.chat.id, 'По тетради: подготовка к контрольной работе.')
    if message.text == '3.Физика':
        bot.send_message(message.chat.id, 'Подготовиться к контрольная работе по теме "Свойства твердых тел и жидкостей".')
    if message.text == '4.Английский язык':
        bot.send_message(message.chat.id, 'с.47 №8.')
    if message.text == '5.Проект':
        bot.send_message(message.chat.id, 'Делать свой проект.')
    if message.text == '6.История':
        bot.send_message(message.chat.id, 'параграф 15.')
    if message.text == '7.Проект':
        bot.send_message(message.chat.id, 'Делать свой проект.')
bot.polling(none_stop=True, interval=0)

