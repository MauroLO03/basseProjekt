class Match:

    def __init__(
        self,
        id: int,
        home_team_id: int,
        away_team_id: int,
        league_id: int,
        referee: str,
        date
    ):
        self.id = id
        self.home_team_id = home_team_id
        self.away_team_id = away_team_id
        self.league_id = league_id
        self.referee = referee
        self.date = date
