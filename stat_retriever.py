"""
stat-retriever by Team-95
stat_retriever.py
"""

import requests
import json
import csv

def main():
    season = "2014-15"
    stats_path = "nba_stats.csv"

    url = ("http://stats.nba.com/stats/leaguedashplayerbiostats?College=&Conference="
    "&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment="
    "&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound="
    "0&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&Season=%s&SeasonSegment="
    "&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference="
    "&VsDivision=&Weight=") % season

    response = requests.get(url)
    stats = json.loads(response.text)

    with open(stats_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, dialect="excel")

        for row in stats["resultSets"][0]["rowSet"]:
            player_id = row[0]
            player_name = row[1]
            team_id = row[2]
            team_abbreviation = row[3]
            player_age = row[4]
            player_height = row[5]
            player_height_inches = row[6]
            player_weight = row[7]
            player_college = row[8]
            player_country = row[9]
            player_draft_year = row[10]
            player_draft_round = row[11]
            player_draft_number = row[12]
            player_games_played = row[13]
            player_points = row[14]
            player_rebounds = row[15]
            player_assists = row[16]
            player_net_rating = row[17]
            player_oreb_pct = row[18]
            player_dreb_pct = row[19]
            player_usg_pct = row[20]
            player_ts_pct = row[21]
            player_ast_pct = row[22]

            writer.writerow([player_id, player_name, team_id, team_abbreviation, player_age,
                player_height, player_height_inches, player_weight, player_college, player_country,
                player_draft_year, player_draft_round, player_draft_number, player_games_played,
                player_points, player_rebounds, player_assists, player_net_rating, player_oreb_pct,
                player_dreb_pct, player_usg_pct, player_ts_pct, player_ast_pct])

        csvfile.close()


if __name__ == "__main__":
    main()
