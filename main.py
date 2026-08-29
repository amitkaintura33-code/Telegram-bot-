import telebot

TOKEN = "8747352245:AAEOXKZWVidjut5zWfgyXaJJSrnAruYKjUo"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
  bot.reply_to(message, "Hello! Main 24/7 active hun.")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
  bot.reply_to(message, message.text)


bot.infinity_polling()
