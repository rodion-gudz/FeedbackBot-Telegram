# -*- coding: utf-8 -*- 
import telebot;

bot = telebot.TeleBot('token');

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
 if message.text ==u"/помощь":
   bot.send_message(message.chat.id, u"Доступные команды  /новости /информация")
 if message.text ==u"/новости":
   bot.send_message(message.chat.id, u"IP SAMP RP сервера сменился 45.142.214.154:7777!")
 if message.text ==u"/информация":
    bot.send_message(message.chat.id, u"Открыт SAMP RP Сервер! IP: 45.142.214.154:7777 Полезные ссылки: Наш сайт - laciamemeframe.space (Сайт создателя проекта, так как сайт самого сервера находится в разработке). Форум - В разработке, Группа Вконтакте - https://vk.com/pixsetup, Свободная группа Вконтакте - В разработке. IP: 45.142.214.154:7777")
 #elif message.text =="/help":
   #bot.send_message(message.from_user.id, "Доступные команды  /news и /info")
 #else:
    #bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
bot.polling(none_stop=True, interval=0)
