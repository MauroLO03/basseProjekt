from repository.statRepository import StatRepository
from util.poisson import (
    calculate_attack_strength,
    calculate_defense_strength,
    calculate_expected_goals,
    calculate_goal_probabilities,
    build_score_matrix,
    calculate_match_probabilities
)
from util.odds import prediction_to_odds



class MatchWinnerService:
    
    @staticmethod
    def calculate_match_winner(home_team_id: int, away_team_id: int):
        NUM_MATCHES = 10

        #först plockar vi ut rådata:
        league_average_home_goal = StatRepository.get_league_home_goal_average()
        league_average_away_goal = StatRepository.get_league_away_goal_average()

        home_team_attack_stat = StatRepository.get_home_goals_scored(team_id = home_team_id, num_matches=NUM_MATCHES )
        home_team_defence_stat = StatRepository.get_home_goals_conceded(team_id=home_team_id, num_matches=NUM_MATCHES)

        away_team_attack_stat = StatRepository.get_away_goals_scored(team_id=away_team_id, num_matches=NUM_MATCHES)
        away_team_defence_stat = StatRepository.get_away_goals_conceded(team_id=away_team_id, num_matches=NUM_MATCHES)

        #behandla rådatan:
        home_attack_strength = calculate_attack_strength(home_team_attack_stat, league_average_home_goal)
        home_defence_strength = calculate_defense_strength(home_team_defence_stat, league_average_away_goal)

        away_attack_strength = calculate_attack_strength(away_team_attack_stat, league_average_away_goal)
        away_defence_strength = calculate_defense_strength(away_team_defence_stat, league_average_home_goal)


        away_team_xG = calculate_expected_goals(away_attack_strength,home_defence_strength, league_average_away_goal)
        home_team_xG = calculate_expected_goals(home_attack_strength, away_defence_strength, league_average_home_goal)



        #behandla den behandlade datan:
        home_goal_probability = calculate_goal_probabilities(home_team_xG)
        away_goal_probability = calculate_goal_probabilities(away_team_xG)

        #slutligen sammanställ dem:
        score_probability_matrix = build_score_matrix(home_goal_probability, away_goal_probability)

        prediction = calculate_match_probabilities(score_probability_matrix)

        match_winner_odds = prediction_to_odds(prediction)
        return match_winner_odds




