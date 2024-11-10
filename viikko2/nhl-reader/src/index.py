import requests
from player import Player

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
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    print(f"Players from FIN\n")
    for player in players:
        print(player)

if __name__ == "__main__":
    main()
