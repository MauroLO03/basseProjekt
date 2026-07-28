from repository.statRepository import StatRepository 
from domains.predictions.htFtDomain import HtFtProbabilities , MatchHtFtOdds


class HtFtService:

    @staticmethod
    def get_team_odds(home_team_id: int, away_team_id: int) -> MatchHtFtOdds:

        num_matches = 20

        #Vi kallar på repository funktionen som hämtar dem X senaste matcherna för hemma och borta lagen
        #Repository ansvarar för att beräkna sannolikheten
        home_rows = StatRepository.get_team_htft_probabilities(home_team_id, 'HOME', num_matches)
        away_rows = StatRepository.get_team_htft_probabilities(away_team_id, 'AWAY', num_matches)


        #Skapar objekten
        home_probabilities = HtFtProbabilities.from_db_rows(home_rows)
        away_probabilities = HtFtProbabilities.from_db_rows(away_rows)

        

        return MatchHtFtOdds(home = home_probabilities.to_odds(), away=  away_probabilities.to_odds())
