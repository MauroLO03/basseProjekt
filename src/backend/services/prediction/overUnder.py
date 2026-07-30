from services.prediction.xGService import xGCalculator
from util.poisson import (calculate_poisson_goal_distribution, build_score_matrix)
from domains.predictions.overUnderDomain import overUnder


class overUnderService:
    @staticmethod
    def _calc_over_under_probability(
        score_matrix: list[list[float]],
        line: float
    ) -> overUnder:

        over_probability = 0.0
        under_probability = 0.0

        for home_goals, row in enumerate(score_matrix):
            for away_goals, probability in enumerate(row):

                total_goals = home_goals + away_goals

                if total_goals > line:
                    over_probability += probability
                else:
                    under_probability += probability

        return overUnder(line, over_probability, under_probability)

    @staticmethod
    def calculate_over_under(home_team_id: int , away_team_id: int, num_matches: int) -> overUnder:

        #beräkna xG
        match_xg =xGCalculator.calculate_match_xG(home_team_id, away_team_id, num_matches)

        #beräkna sannolikheterna
        home_prob = calculate_poisson_goal_distribution(match_xg.home_xG)
        away_prob = calculate_poisson_goal_distribution(match_xg.away_xG)

        score_matrix = build_score_matrix(home_prob, away_prob)

        over15 = overUnderService._calc_over_under_probability(score_matrix, 1.5)
        over25 = overUnderService._calc_over_under_probability(score_matrix, 2.5)
        over35 = overUnderService._calc_over_under_probability(score_matrix, 3.5)

        return {over15, over25, over35}

