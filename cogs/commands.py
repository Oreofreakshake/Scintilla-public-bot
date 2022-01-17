import random
from cogs import commandnames
from api import prayer

n = 1  # to make it easier for you to read the list, just ignore 0 and start from 1


class Commands:
    def __init__(self, bot):
        self.bot = bot

    def welcome_text(self, message):  # ✅
        self.bot.reply_to(
            message,
            f"""These are the commands you can try for now! 
/{commandnames.commandsname[1-n]} 
/{commandnames.commandsname[2-n]} 
         """,
        )

    def saam_meter(self, message):  # ✅
        tempINT = random.choice(range(101))
        value = str(tempINT)
        if tempINT > 90:
            self.bot.reply_to(message, "You are " + value + "% saam, damn unlucky")
        else:
            self.bot.reply_to(message, "You are " + value + "% saam")

    def prayertime(self, message):  # ❌
        self.bot.reply_to(message, f"Your next prayer time is {prayer.NextPrayerTime}")