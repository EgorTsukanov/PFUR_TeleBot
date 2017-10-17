# coding=utf-8
import telebot

import config

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])

def start(message):
    sent = bot.send_message(message.chat.id, "Hello there, whats your name?")
    bot.register_next_step_handler(sent,hello)

def hello(message):
    bot.send_message(message.chat.id, "Hello, {name}".format(name=message.text))

if __name__ == '__main__':
     bot.polling(none_stop=True)