
from Schemas.matchSchema import MatchResponse


def match_to_response(match, prediction):

    return MatchResponse(
        id=match.id,
        homeTeam=match.home_team,
        awayTeam=match.away_team,
        matchWinner=match.match_winner,
        league=match.league,
        prediction=prediction
    )