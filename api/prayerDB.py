import sqlite3
from datetime import date


# cat = 82 & 57


def get_day():
    now = date.today()
    jan = date(now.year, 1, 1)
    diff = now - jan
    return diff.days


def connectDB():
    conn = sqlite3.connect("./salat.db")
    return conn


def convert_time(minutes):
    hours = minutes // 60
    mins = minutes % 60
    hoursvalue = str(hours).rjust(2, "0")
    minsvalue = str(mins).rjust(2, "0")
    timeString = str(hoursvalue) + ":" + str(minsvalue)
    return timeString


def getPrayerTime(catID, days):
    connection = connectDB()
    c = connection.cursor()

    c.execute(
        f"select Fajuru,Dhuhr,Asr,Maghrib,Isha from PrayerTimes where CategoryId={catID} and Date={days}"
    )

    Times = c.fetchone()

    prayersArray = [
        "Fajuru",
        "Dhuhr",
        "Asr",
        "Maghrib",
        "Isha",
    ]
    prayerTimeaArray = {}

    for item in range(len(prayersArray)):
        ftime = convert_time(Times[item])

        prayerTimeaArray[prayersArray[item]] = ftime

    connection.close()

    return prayerTimeaArray

print(f"Prayer cogs are ready!\n")

