from repository.statRepository import StatRepository
from util.poisson import (calculate_poisson_goal_distribution, build_score_matrix)
from domains.predictions.cardDomain import CardDomain
from domains.predictions.matchYellowDomain import MatchYellowDomain
from util.odds import probability_to_odds


class CardService:

    @staticmethod
    def _calculate_card_probability(distribution, line) -> CardDomain:

        over = 0
        under = 0

        for cards, probability in enumerate(distribution):

            if cards > line:
                over += probability
            else:
                under += probability

        return CardDomain(line, over, under)

    @staticmethod
    def calculate_yellow_cards(home_team_id: int, away_team_id: int, num_matches: int) -> MatchYellowDomain:

        #hämta data
        home_yellow = StatRepository.get_home_yellow_cards(home_team_id, num_matches)
        away_yellow = StatRepository.get_away_yellow_cards(away_team_id, num_matches)

        home_yellow_conceded = StatRepository.get_home_yellow_cards_conceded(home_team_id, num_matches)
        away_yellow_conceded = StatRepository.get_away_yellow_cards_conceded(away_team_id, num_matches)

        expected_home_yellow = (home_yellow+away_yellow_conceded)/2
        expected_away_yellow = (away_yellow+home_yellow_conceded)/2

        expected_total_yellow = expected_away_yellow+ expected_home_yellow

        yellow_distribution = calculate_poisson_goal_distribution(expected_total_yellow, 10)


        over35 = CardService._calculate_card_probability(yellow_distribution, 3.5)
        over45 = CardService._calculate_card_probability(yellow_distribution, 4.5)
        over55 = CardService._calculate_card_probability(yellow_distribution, 5.5)

        over35_odds = CardDomain(line=over35.line, over=probability_to_odds(over35.over), under= probability_to_odds(over35.under))
        over45_odds = CardDomain(line=over45.line, over=probability_to_odds(over45.over), under= probability_to_odds(over45.under))
        over55_odds = CardDomain(line=over55.line, over=probability_to_odds(over55.over), under= probability_to_odds(over55.under))

        return MatchYellowDomain(overUnder=[over35_odds, over45_odds, over55_odds])



