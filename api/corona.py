import requests

# corona tracker for maldives only
url = "https://coronavirus-19-api.herokuapp.com/countries/Maldives"

session = requests.get(url)
json_data = session.json()

totalCases = json_data["cases"]
todayCases = json_data["todayCases"]
totalDeaths = json_data["deaths"]
todayDeaths = json_data["todayDeaths"]
recovered = json_data["recovered"]
active = json_data["active"]
critical = json_data["critical"]


print(f"Corona cogs are ready!\n")