from repository.statRepository import StatRepository
from util.poisson import (
    calculate_poisson_goal_distribution,
    build_score_matrix,
    calculate_match_probabilities
)
from util.odds import prediction_to_odds
from services.prediction.xGService import xGCalculator



class MatchWinnerService:
    
    @staticmethod
    def calculate_match_winner(home_team_id: int, away_team_id: int):
        NUM_MATCHES = 10

        #beräkna xG
        match_xg = xGCalculator.calculate_match_xG(home_team_id, away_team_id, NUM_MATCHES)


        #behandla den behandlade datan:
        home_goal_probability = calculate_poisson_goal_distribution(match_xg.home_xG)
        away_goal_probability = calculate_poisson_goal_distribution(match_xg.away_xG)

        #slutligen sammanställ dem:
        score_probability_matrix = build_score_matrix(home_goal_probability, away_goal_probability)

        prediction = calculate_match_probabilities(score_probability_matrix)

        match_winner_odds = prediction_to_odds(prediction)
        return match_winner_odds




