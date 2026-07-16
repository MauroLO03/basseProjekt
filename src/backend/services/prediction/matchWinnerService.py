from repository.statRepository import StatRepository
from domains.matchDomain import Match


class MatchWinner:
    
    @staticmethod
    def calculate_match_winner(match: Match):
        NUM_MATCHES = 10

        home_history = StatRepository.get
