from domains.predictionDomain import Prediction
from services.prediction.matchWinnerService import MatchWinnerService
from domains.matchDomain import Match

class PredictionService:

    @staticmethod
    def calculate_match_odds(match: Match) -> Prediction:
        home_team_id = match.home_team_id
        away_team_id = match.away_team_id

        match_winner =  MatchWinnerService.calculate_match_winner(home_team_id, away_team_id)

        return Prediction(
            matchWinner = match_winner
        )
        