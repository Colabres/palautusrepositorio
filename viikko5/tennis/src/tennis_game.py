class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.case_basic_score={0:"Love", 1:"Fifteen" ,2:"Thirty",3:"Forty"}
        self.case_advantage_score={1:"Advantage player2", 3:"Advantage player1" ,4:"Win for player1",0:"Win for player2"}
        self.case_deuce_score={0:"Love-All", 1:"Fifteen-All" ,2:"Thirty-All",3:"Deuce"}
    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        score = ""
        temp_score = 0

        if self.player1_score == self.player2_score:
            if self.player1_score>2: score=self.case_deuce_score[3]
            else: score=self.case_deuce_score[self.player1_score]

        elif self.player1_score >= 4 or self.player2_score >= 4:
            minus_result = self.player1_score - self. player2_score +2
            score=self.case_advantage_score[max(0, min(4, minus_result))]

        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.player1_score
                else:
                    score = score + "-"
                    temp_score = self.player2_score
                score= score + self.case_basic_score[temp_score]


        return score
