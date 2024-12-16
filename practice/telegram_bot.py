import dotenv
import telebot

env = dotenv.dotenv_values()
token = env.get("TELEGRAM_API")
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def start(message):
    bot.send_message(message.chat.id, "Отстань")


bot.infinity_polling()
