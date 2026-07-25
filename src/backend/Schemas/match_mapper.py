
from Schemas.matchSchema import MatchResponse
from Schemas.predictionSchema import PredictionResponse, WinnerOdds


def match_to_response(match, prediction):


    response = MatchResponse(
        id=match.id,
        homeTeamId=match.home_team_id,
        awayTeamId=match.away_team_id,
        leagueId=match.league_id,
        date=str(match.date),
        prediction=PredictionResponse(
            matchWinner=WinnerOdds(
                home=prediction.matchWinner.home,
                draw=prediction.matchWinner.draw,
                away=prediction.matchWinner.away
            )
        )
    )


    return response