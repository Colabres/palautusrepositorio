class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict["team"]
        self.goal = dict["goals"]
        self.assists = dict["assists"]
        self.nationality=dict["nationality"]
        self.points = self.assists + self.goal
    def __str__(self):
        return f"{self.name:20} team {self.team:4}{self.goal:3}  + {self.assists:3} = {self.points:2} "
        
