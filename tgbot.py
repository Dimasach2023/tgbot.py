import telebot
import os
import random
bot = telebot.TeleBot("7342064133:AAEhPnefTbiIJJMz49BEqYJnaGo9YCeDWN0")

@bot.message_handler(commands=['mem'])
def send_mem(message):
    names = (os.listdir('images'))
    name = random.choice(names)
    with open(f'images/{name}', 'rb') as f:
        # Отправляем фото, выбранное случайным образом
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['animals_mem'])
def send_mem(message):
    names1 = (os.listdir('animals_images'))
    name1 = random.choice(names1)
    with open(f'animals_images/{name1}', 'rb') as f:
        # Отправляем фото, выбранное случайным образом
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Привет! Используй команду /mem, чтобы получить мем!, Используй команду /animals_mem, чтобы получить мем c животными!")

bot.polling()
