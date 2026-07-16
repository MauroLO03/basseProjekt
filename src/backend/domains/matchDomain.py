class Match:

    def __init__(
        self,
        id: int,
        home_team: int,
        away_team: int,
        league_id: int,
        referee: str,
        date
    ):
        self.id = id
        self.home_team = home_team
        self.away_team = away_team
        self.league_id = league_id
        self.referee = referee
        self.date = date
