from domains.predictionDomain import Prediction
from services.prediction.matchWinnerService import MatchWinnerService
from domains.matchDomain import Match
from services.prediction.HtFtService import HtFtService
from services.prediction.overUnderService import OverUnderService
from services.prediction.cornerService import CornerService
from services.prediction.cardService import CardService

class PredictionService:

    @staticmethod
    def calculate_match_odds(match: Match) -> Prediction:
        NUM_MATCHES = 20

        home_team_id = match.home_team_id
        away_team_id = match.away_team_id

        match_winner =  MatchWinnerService.calculate_match_winner(home_team_id, away_team_id)
        ht_ft_odds = HtFtService.get_team_odds(home_team_id, away_team_id)
        over_under_odds = OverUnderService.calculate_over_under(home_team_id, away_team_id, NUM_MATCHES)
        corner_odds = CornerService.calculate_corner_prediction(home_team_id, away_team_id, NUM_MATCHES)
        yellow_odds = CardService.calculate_yellow_cards(home_team_id, away_team_id, NUM_MATCHES)
        

        return Prediction(
            matchWinner = match_winner,
            htFtOdds = ht_ft_odds,
            overUnderOdds = over_under_odds,
            cornerOdds = corner_odds,
            yellowCardOdds = yellow_odds

        )
        