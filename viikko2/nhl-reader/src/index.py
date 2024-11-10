import requests
from player import Player
from rich import print
from rich.table import Table

class PlayerReader:
    def __init__(self, url):
        self._url = url

    def get_players(self):
        response = requests.get(self._url).json()
        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)

        return players

class PlayerStats:
    def __init__(self, reader):
        self._players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        def sort_by_points(player):
            return player.goals + player.assists

        players = [player for player in self._players if player.nationality == nationality]
        sorted_players = sorted(
            players,
            reverse=True,
            key=sort_by_points
        )
        
        return sorted_players

def main():
    print("NHL statistics by nationality")
    seasons = [
        "2018-19",
        "2019-20",
        "2020-21",
        "2021-22",
        "2022-23",
        "2023-24",
        "2024-25",
    ]

    print(f"Select season [{"/".join(seasons)}]", end=": ")
    selected_season = input()
    if selected_season not in seasons:
        return

    url = f"https://studies.cs.helsinki.fi/nhlstats/{selected_season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    nationalities = set([player.nationality for player in reader.get_players()])
    print(f"Select nationality [{"/".join(nationalities)}]", end=": ")
    selected_nationality = input()
    if selected_nationality not in nationalities:
        return

    table = Table(title=f"Top scorers from {selected_nationality} in the season {selected_season}")
    table.add_column("Name")
    table.add_column("Team")
    table.add_column("Goals")
    table.add_column("Assists")
    table.add_column("Points")
    
    players = stats.top_scorers_by_nationality(selected_nationality)
    for player in players:
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.goals + player.assists))

    print(table)

if __name__ == "__main__":
    main()
