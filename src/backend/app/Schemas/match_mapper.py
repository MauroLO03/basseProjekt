from app.Schemas.matchSchema import MatchResponse
from app.Schemas.predictionSchema import PredictionResponse, WinnerOdds, HalfTimeFullTimeOdds
from app.Schemas.predictionSchema import GoalsOdds, GoalLine

def match_to_response(match, prediction) -> MatchResponse:
    match_id = getattr(match, "id", None) or getattr(match, "match_id", None)
    match_date = getattr(match, "date", None) or getattr(match, "match_date", None)

    # 1. Convert matchWinner
    winner_data = prediction.matchWinner
    if not isinstance(winner_data, WinnerOdds):
        winner_odds = WinnerOdds(
            home=getattr(winner_data, "home", 0.0),
            draw=getattr(winner_data, "draw", 0.0),
            away=getattr(winner_data, "away", 0.0)
        )
    else:
        winner_odds = winner_data

    # 2. Convert MatchHtFtOdds -> HalfTimeFullTimeOdds or Dict
    ht_ft_data = getattr(prediction, "htFtOdds", None) or getattr(prediction, "htFtProbabilities", None)
    
    # If ht_ft_data is a MatchHtFtOdds object, convert it to a dict or model
    if hasattr(ht_ft_data, "__dict__"):
        ht_ft_value = {
            "home": getattr(ht_ft_data.home, "__dict__", ht_ft_data.home),
            "away": getattr(ht_ft_data.away, "__dict__", ht_ft_data.away),
        }
    else:
        ht_ft_value = ht_ft_data

    over_under_data = GoalsOdds(
    overUnder=[
        GoalLine(
            line=item.line,
            over=item.over,
            under=item.under
        )
        for item in prediction.overUnderOdds.overUnder
    ]
)

    return MatchResponse(
        id=match_id,
        homeTeamId=match.home_team_id,
        awayTeamId=match.away_team_id,
        leagueId=match.league_id,
        date=str(match_date) if match_date else "",
        prediction=PredictionResponse(
            matchWinner=winner_odds,
            htFtOdds=ht_ft_value,
            overUnderOdds=over_under_data
        )
    )