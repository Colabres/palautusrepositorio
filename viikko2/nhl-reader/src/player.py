class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict["team"]
        self.goal = dict["goals"]
        self.assists = dict["assists"]
        self.nationality=dict["nationality"]
    
    def __str__(self):
        #return f"{self.name} team {self.team} goals {self.goal} assists {self.assists} Nationality {self.nationality}"
        return f"{self.name:20}"
