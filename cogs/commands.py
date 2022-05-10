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
from api import prayerDB
from api import corona

from prettytable import PrettyTable

from datetime import datetime, date
import pytz


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
/{commandnames.commandsname[3-n]} 
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

    def prayertime(self, message):  # ✅
        add_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        Prayerbutton = ["Male'", "Addu"]
        buttonArray = []

        for items in range(len(Prayerbutton)):
            button = types.KeyboardButton(Prayerbutton[items])
            buttonArray.append(button)

        add_markup.add(
            buttonArray[0],
            buttonArray[1],
        )

        self.bot.send_message(
            message.chat.id,
            "For which location?",
            reply_markup=add_markup,
        )

    def bot_reply_to_prayertime(self, message):

        timeinmv = pytz.timezone("Indian/Maldives")

        timer = datetime.now(timeinmv).strftime("%H:%M").lower()

        CurrentTime = f"{timer}"

        iterateList = ["Fajuru", "Dhuhr", "Asr", "Maghrib", "Isha"]
        day = prayerDB.get_day()


        #--------driver code---------

        if message.text == "Male'":
                prayerTimes = prayerDB.getPrayerTime(57, day)

                timeArray = []
                for i in iterateList:
                    timeArray.append(prayerTimes[i])

                DataGivenM = PrettyTable(["Prayer", "Time (Male')"])

                DataGivenM.add_row(["Fajuru", timeArray[0]])
                DataGivenM.add_row(["Dhuhr ", timeArray[1]])
                DataGivenM.add_row(["Asr", timeArray[2]])
                DataGivenM.add_row(["Maghrib", timeArray[3]])
                DataGivenM.add_row(["Isha", timeArray[4]])

                self.bot.send_message(
                    message.chat.id,
                    f"```{DataGivenM}```",
                    reply_markup=ReplyKeyboardRemove(),
                    parse_mode="Markdown",
                )

        if message.text == "Addu":
            prayerTimes = prayerDB.getPrayerTime(82, day)

            timeArray = []
            for i in iterateList:
                timeArray.append(prayerTimes[i])

            DataGivenA = PrettyTable(["Prayer", "Time (Addu)"])

            DataGivenA.add_row(["Fajuru", timeArray[0]])
            DataGivenA.add_row(["Dhuhr ", timeArray[1]])
            DataGivenA.add_row(["Asr", timeArray[2]])
            DataGivenA.add_row(["Maghrib", timeArray[3]])
            DataGivenA.add_row(["Isha", timeArray[4]])

            self.bot.send_message(
                message.chat.id,
                f"```{DataGivenA}```",
                reply_markup=ReplyKeyboardRemove(),
                parse_mode="Markdown",
            )

            

    # -----------------------------------------------------------------------------------------------

    def covid(self, message):
        data = f"""*This data is only valid in Maldives*\n
Total Cases : ```{corona.totalCases}```
Total Deaths : ```{corona.totalDeaths}```
Active : ```{corona.active}```
Recovered : ```{corona.recovered}```
Critical : ```{corona.critical}```
        """

        self.bot.send_message(message.chat.id, f"{data}", parse_mode="Markdown")
