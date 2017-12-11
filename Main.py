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
        user_markup.row('1.Информатика', '2.Информатика', '3.География')
        user_markup.row('4.Литература', '5.Алгебра', '6.Геометрия')
        user_markup.row('7.Физическая культура')
        user_markup.row('Вернуться назад')

        bot.send_message(message.from_user.id,"Выберите урок", reply_markup=user_markup)

    if message.text == 'Узнать расписание на завтра📰':
        answer = "1.08:30 - Информатика \n2.09:25 - Информатика \n3.10:30 - География \n4.11:35 - Литература \n5.12:30 - Алгебра \n6.13:25 - Геометрия \n7.14:30 - Физическая культура"
        bot.send_message(message.chat.id, answer)
    if message.text == 'Вернуться назад':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Спросить дз на завтра')
        user_markup.row('Узнать расписание на завтра📰')
        bot.send_message(message.from_user.id,
                         "Что будем делать дальше?",
                         reply_markup=user_markup)

    if message.text == '1.Информатика':
        bot.send_message(message.chat.id, 'Учить логические формулы и функции.')
    if message.text == '2.Информатика':
        bot.send_message(message.chat.id, 'Учить преобразование логических выражений.')
    if message.text == '3.География':
        bot.send_message(message.chat.id, 'Приготовить сообщение о составе населения России.')
    if message.text == '4.Литература':
        bot.send_message(message.chat.id, 'Народные образы в поэме. Народные представления о счастье')
    if message.text == '5.Алгебра':
        bot.send_message(message.chat.id, '№4.23(а), №4.25, вар.3')
    if message.text == '6.Геометрия':
        bot.send_message(message.chat.id, 'Повторить тему параллельность плоскостей. Параллелепипед. Тетраэдр.')
    if message.text == '7.Физическая культура':
        bot.send_message(message.chat.id, 'По физкультуре ничего не задают 😓😩😭😭😭😭')
bot.polling(none_stop=True, interval=0)

