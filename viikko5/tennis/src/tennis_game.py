class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 = self.m_score1 + 1
        elif player_name == self.player2_name:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        score = ""

        if self.m_score1 == self.m_score2:
            match self.m_score1:
                case 0:
                    score = "Love-All"
                case 1:
                    score = "Fifteen-All"
                case 2:
                    score = "Thirty-All"
                case _:
                    score = "Deuce"
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            minus_result = self.m_score1 - self. m_score2
            match minus_result:
                case 1:
                    score = f"Advantage {self.player1_name}"
                case -1:
                    score = f"Advantage {self.player2_name}"
                case minus_result if minus_result >= 2:
                    score = f"Win for {self.player1_name}"
                case _:
                    score = f"Win for {self.player2_name}"
        else:
            temp_score = 0
            def get_name(score):
                match score:
                    case 0:
                        return "Love"
                    case 1:
                        return "Fifteen"
                    case 2:
                        return "Thirty"
                    case 3:
                        return "Forty"

            score = f"{get_name(self.m_score1)}-{get_name(self.m_score2)}"

        return score
