import os
import telebot
from cogs import commands
from dotenv import load_dotenv


TOKEN = process.env.TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["hello", "start"])
def start_command(message):
    command = commands.Commands(bot)
    command.welcome_text(message)


@bot.message_handler(commands=["saamometer"])
def command_one(message):
    command = commands.Commands(bot)
    command.saam_meter(message)


if __name__ == "__main__":
    try:
        print("I am online")
        bot.infinity_polling()
    except:
        print("run time error")
