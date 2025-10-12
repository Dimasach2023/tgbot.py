import telebot

# Инициализация бота с использованием его токена
bot = telebot.TeleBot("7342064133:AAEhPnefTbiIJJMz49BEqYJnaGo9YCeDWN0")

# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')

# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, f'Существующие команды: /start /hello - Привет! Я бот; /heh - выводит хех столько раз сколько пользователь указал после команды heh {bot.get_me().first_name}!')

# Запуск бота
bot.polling()
