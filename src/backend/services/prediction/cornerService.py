from util.poisson import (calculate_poisson_goal_distribution, build_score_matrix)
from repository.statRepository import StatRepository 
from domains.predictions.cornerDomain import CornerDomain
from util.odds import probability_to_odds
from  domains.predictions.matchCornerDomain import MatchCornerDomain


class CornerService:
    @staticmethod
    def _calculate_total_corner_probability(matrix, line) -> CornerDomain:

        over_probability = 0.0

        for home, row in enumerate(matrix):

            for away, value in enumerate(row):

                total = home + away

                if total > line:
                    over_probability += value


        return CornerDomain(
            line=line,
            over=over_probability,
            under=1 - over_probability
        )
    
    @staticmethod
    def calculate_corner_prediction(home_team_id: int, away_team_id: int, num_matches: int)->MatchCornerDomain:

        #hämta data från db
        home_corners = StatRepository.get_home_corners(home_team_id, num_matches)
        away_corners_conceded = StatRepository.get_away_corners_conceded(away_team_id,num_matches)

        away_corners = StatRepository.get_away_corners(away_team_id, num_matches)
        home_corners_conceded = StatRepository.get_home_corners_conceded(home_team_id, num_matches)

        #behandla data
        expected_home_corners = (home_corners + away_corners_conceded)/2
        expected_away_corners = (away_corners + home_corners_conceded)/2

        #modellera enligt poisson fördelning för max 15 hörnor
        home_distribution = calculate_poisson_goal_distribution(expected_home_corners, 15)
        away_distribution = calculate_poisson_goal_distribution(expected_away_corners, 15)


        #sammanställ sannolikheterna
        matrix = build_score_matrix(home_distribution, away_distribution)

        over85 = CornerService._calculate_total_corner_probability(matrix, 8.5)
        over95 = CornerService._calculate_total_corner_probability(matrix, 9.5)
        over105= CornerService._calculate_total_corner_probability(matrix, 10.5)

        over85_odds = CornerDomain(line=over85.line, over=probability_to_odds(over85.over), under= probability_to_odds(over85.under))
        over95_odds = CornerDomain(line=over95.line, over=probability_to_odds(over95.over), under= probability_to_odds(over95.under))
        over105_odds = CornerDomain(line=over105.line, over=probability_to_odds(over105.over), under= probability_to_odds(over105.under))

        return MatchCornerDomain(overUnder=[over85_odds, over95_odds, over105_odds])


        
    