from domains.predictionDomain import Prediction
from services.prediction.matchWinnerService import MatchWinnerService

class PredictionService:

    @staticmethod
    def calculate_match_odds(match) -> Prediction:
        match_winner = MatchWinnerService.calculate_match_winner_odds(match.home_team, match.away_team)

        return Prediction(
            match_winner=match_winner
        )
        