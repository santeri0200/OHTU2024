import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    print(f"Players from FIN\n")
    [print(player) for player in players if player.nationality == "FIN"]

if __name__ == "__main__":
    main()
