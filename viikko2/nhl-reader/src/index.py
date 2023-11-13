import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        #print(player_dict)
        players.append(player)

    print("Oliot:")
    nat = input("Give nationality")
    print(f"Players from {nat}")

    for player in players:
        if player.nationality == nat.upper():
            print(player)

if __name__ == "__main__":
    main()
