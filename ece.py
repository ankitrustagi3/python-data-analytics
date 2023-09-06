import requests
from datetime import date

mlb_url = "http://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard"
nba_url = ""

response = requests.get(mlb_url)

json = response.json()

for i in range(len(json["events"])):
    print(json["events"][i]["name"])

    # Print the scores of the teams
    print(json["events"][i]["competitions"][0]["competitors"][0]["score"])
    print(json["events"][i]["competitions"][0]["competitors"][1]["score"])
    pass

