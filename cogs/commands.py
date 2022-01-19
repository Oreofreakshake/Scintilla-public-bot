import random

from cogs import commandnames
from telebot import types
from telebot.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    KeyboardButton,
)
from api import prayer

from prettytable import PrettyTable

n = 1  # to make it easier for you to read the list, just ignore 0 and start from 1


class Commands:
    def __init__(self, bot):
        self.bot = bot

    def welcome_text(self, message):  # ✅
        self.bot.send_message(
            message.chat.id,
            f"""These are the commands you can try for now! 
/{commandnames.commandsname[1-n]} 
/{commandnames.commandsname[2-n]} 
         """,
        )

    # -----------------------------------------------------------------------------------------------

    def saam_meter(self, message):  # ✅
        tempINT = random.choice(range(101))
        value = str(tempINT)
        if tempINT > 90:
            self.bot.reply_to(message, "You are " + value + "% saam, damn unlucky")
        else:
            self.bot.reply_to(message, "You are " + value + "% saam")

    # -----------------------------------------------------------------------------------------------

    def prayertime(self, message):  # ✅ (Will update and make it better later)
        add_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Fajar")
        button2 = types.KeyboardButton("Dhuhar")
        button3 = types.KeyboardButton("Asr")
        button4 = types.KeyboardButton("Maghrib")
        button5 = types.KeyboardButton("Isha")
        button6 = types.KeyboardButton("Every prayer")
        add_markup.add(button1, button2, button3, button4, button5, button6)
        self.bot.send_message(
            message.chat.id,
            "What prayer time do you want to know?",
            reply_markup=add_markup,
        )

    def bot_reply_to_prayertime(self, message):
        replyFajar = f"you have around {prayer.TimeLeftFajar} hours left"
        replyDhuhar = f"you have around {prayer.TimeLeftDhuhar} hours left"
        replyAsr = f"you have around {prayer.TimeLeftAsr} hours left"
        replyMaghrib = f"you have around {prayer.TimeLeftMaghrib} hours left"
        replyIsha = f"you have around {prayer.TimeLeftIsha} hours left"

        if prayer.TimeLeftFajar == 1:
            replyFajar = "It's almost time now, be ready and make sure you pray!"
        if prayer.TimeLeftDhuhar == 1:
            replyDhuhar = "It's almost time now, be ready and make sure you pray!"
        if prayer.TimeLeftAsr == 1:
            replyAsr = "It's almost time now, be ready and make sure you pray!"
        if prayer.TimeLeftMaghrib == 1:
            replyMaghrib = "It's almost time now, be ready and make sure you pray!"
        if prayer.TimeLeftIsha == 1:
            replyIsha = "It's almost time now, be ready and make sure you pray!"

        Fajar = f"Fajar time is {prayer.Fajar12hour}\n{replyFajar}"
        Dhuhar = f"Dhuhar time is {prayer.Dhuhar12hour}\n{replyDhuhar}"
        Asr = f"Asr time is {prayer.Asr12hour}\n{replyAsr}"
        Maghrib = f"Maghrib time is {prayer.Maghrib12hour}\n{replyMaghrib}"
        Isha = f"Isha time is {prayer.Isha12hour}\n{replyIsha}"

        DataGiven = PrettyTable(["Prayer", "Time"])

        DataGiven.add_row(["Fathis", prayer.Fajar12hour])
        DataGiven.add_row(["Dhuhar", prayer.Dhuhar12hour])
        DataGiven.add_row(["Asr", prayer.Asr12hour])
        DataGiven.add_row(["Maghrib", prayer.Maghrib12hour])
        DataGiven.add_row(["Isha", prayer.Isha12hour])

        if message.text == "Fajar":
            self.bot.reply_to(message, Fajar, reply_markup=ReplyKeyboardRemove())
        if message.text == "Dhuhar":
            self.bot.reply_to(message, Dhuhar, reply_markup=ReplyKeyboardRemove())
        if message.text == "Asr":
            self.bot.reply_to(message, Asr, reply_markup=ReplyKeyboardRemove())
        if message.text == "Maghrib":
            self.bot.reply_to(message, Maghrib, reply_markup=ReplyKeyboardRemove())
        if message.text == "Isha":
            self.bot.reply_to(message, Isha, reply_markup=ReplyKeyboardRemove())
        if message.text == "Every prayer":
            self.bot.send_message(
                message.chat.id,
                f"```{DataGiven}```",
                reply_markup=ReplyKeyboardRemove(),
                parse_mode="Markdown",
            )


# -----------------------------------------------------------------------------------------------
