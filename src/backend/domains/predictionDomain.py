class Prediction:
    def __init__(
        self,
        match_winner,
        half_time_full_time= None,
        goals =  None,
        corners = None,
        both_teams_score = None
    ):
        self.match_winner = match_winner
        self.half_time_full_time = half_time_full_time
        self.goals = goals
        self.corners = corners
        self.both_teams_score = both_teams_score
    