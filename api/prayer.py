from bs4 import BeautifulSoup
import requests

url = "https://www.islamicfinder.org/world/maldives/1282027/male-prayer-times/"

session = requests.get(url)

soup = BeautifulSoup(session.content, "html.parser")


lists = soup.find_all(
    "div",
    class_="fajar-tile",
)

for list in lists:
    NextPrayerTimeData = list.find("span", class_="prayertime").text
    NextPrayerTime = NextPrayerTimeData.lower()
