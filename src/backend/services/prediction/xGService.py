from repository.statRepository import StatRepository
from util.poisson import (   calculate_attack_strength,
    calculate_defense_strength,
    calculate_expected_goals,
)
from domains.predictions.xGDomain import xG

class xGCalculator:


    @staticmethod
    def calculate_match_xG(home_team_id: int, away_team_id: int, num_matches: int) -> xG:

        #hämta relevant data
        league_average_home_goal = StatRepository.get_league_home_goal_average()
        league_average_away_goal = StatRepository.get_league_away_goal_average()


        home_attack = StatRepository.get_home_goals_scored(home_team_id, num_matches)
        away_attack = StatRepository.get_away_goals_scored(away_team_id, num_matches)

        home_defense = StatRepository.get_home_goals_conceded(home_team_id, num_matches)
        away_defense = StatRepository.get_away_goals_conceded(away_team_id,num_matches)

        #beräkna delar som sedan används med xG modellen
        home_attack_strength = calculate_attack_strength(home_attack, league_average_home_goal)
        away_attack_strength = calculate_attack_strength(away_attack, league_average_away_goal)

        home_defense_strength = calculate_defense_strength(home_defense, league_average_away_goal)
        away_defense_strength = calculate_defense_strength(away_defense, league_average_home_goal)



        home_xg = calculate_expected_goals(home_attack_strength, away_defense_strength, league_average_home_goal)
        away_xg = calculate_expected_goals(away_attack_strength, home_defense_strength, league_average_away_goal)

        match_xg = away_xg+home_xg

        return xG(home_xg, away_xg, match_xg)