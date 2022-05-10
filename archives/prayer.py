""" 
This is basically scraping the website for calculated prayertimes which is not very accurate so since I now have the database for the prayer timings, I'll be changing the command completely based on the database timings, thank you (yes this file is 100% useless but I'll keep it for possible future reference)
"""


from bs4 import BeautifulSoup
import requests
from datetime import datetime, date
import pytz

url = "https://www.islamicfinder.org/world/maldives/1282027/male-prayer-times/"

session = requests.get(url)

soup = BeautifulSoup(session.content, "html.parser")


# fajar data

lists = soup.find_all(
    "div",
    class_="fajar-tile",
)

for list in lists:
    FajarData = list.find("span", class_="prayertime").text
    Fajar12hour = FajarData.lower()  # fajar prayer time -------------------------
    # print(Fajar)

# dhuhar data

lists = soup.find_all(
    "div",
    class_="dhuhar-tile",
)

for list in lists:
    DhuharData = list.find("span", class_="prayertime").text
    Dhuhar12hour = DhuharData.lower()  # dhuhar prayer time --------------------------
    # print(Dhuhar)

# asr data

lists = soup.find_all(
    "div",
    class_="asr-tile",
)

for list in lists:
    AsrData = list.find("span", class_="prayertime").text
    Asr12hour = AsrData.lower()  # asr prayer time -------------------------
    # print(Asr)

# maghrib data

lists = soup.find_all(
    "div",
    class_="maghrib-tile",
)

for list in lists:
    MaghribData = list.find("span", class_="prayertime").text
    Maghrib12hour = MaghribData.lower()  # maghrib prayer time -------------------------
    # print(Maghrib)

# isha data

lists = soup.find_all(
    "div",
    class_="isha-tile",
)

for list in lists:
    IshaData = list.find("span", class_="prayertime").text
    Isha12hour = IshaData.lower()  # isha prayer time ------------------------------
    # print(Isha)


def convert24(str1):
    if str1[-2:] == "am" and str1[:2] == "12":
        return "00" + str1[2:-2]

    elif str1[-2:] == "am":
        return str1[:-2]

    elif str1[-2:] == "pm" and str1[:2] == "12":
        return str1[:-2]

    else:
        return str(int(str1[:2]) + 12) + str1[2:5]


# converting to 24hours
Fajar = convert24(Fajar12hour)
Dhuhar = convert24(Dhuhar12hour)
Asr = convert24(Asr12hour)
Maghrib = convert24(Maghrib12hour)
Isha = convert24(Isha12hour)
# ----------------------------------------------------------------------------------------


print(f"Prayer cogs are ready!\n")
