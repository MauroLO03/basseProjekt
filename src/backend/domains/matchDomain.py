class Match:

    def __init__(
        self,
        id,
        home_team,
        away_team,
        league,
        match_winner=None
    ):
        self.id = id
        self.home_team = home_team
        self.away_team = away_team
        self.league = league
        self.match_winner = match_winner
