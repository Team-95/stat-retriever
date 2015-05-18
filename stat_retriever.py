"""
stat-retriever by Team-95
stat_retriever.py
"""

import requests
import json

def main():
    season = "2014-15"
    url = ("http://stats.nba.com/stats/leaguedashplayerbiostats?College=&Conference="
    "&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment="
    "&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound="
    "0&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&Season=%s&SeasonSegment="
    "&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference="
    "&VsDivision=&Weight=") % season

    response = requests.get(url)
    stats = json.loads(response.text)

if __name__ == "__main__":
    main()
