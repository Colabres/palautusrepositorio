import requests
from player import Player


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)

class PlayerReader():
    
    def __init__(self, url):
        self.url=url
        self.players=[]


    def get_players(self):
        response = requests.get(self.url).json()
                

        for player_dict in response:
            player = Player(player_dict)
            self.players.append(player)

        return self.players

class PlayerStats():


    def __init__(self,reader):
        self.reader=reader

    def top_scorers_by_nationality(self, nat):


        print(f"Players from {nat}")
        playerList=[]
        allPlayers=self.reader.get_players()
        for player in allPlayers:
            if player.nationality == nat.upper():
                playerList.append(player)
        sortedPlayer=sorted(playerList,key=lambda x: x.points)
        sortedPlayer.reverse()
        
        return sortedPlayer
        
        #for player in sortedPlayer:
            #print(player)



if __name__ == "__main__":
    main()
