from domains.matchDomain import Match
from repositories import matchRepository
from services.prediction_service import calculate_match_odds
from schemas.match_mapper import match_to_response


class MatchService:

    @staticmethod
    def get_match_by_id(match_id: int) -> MatchResponse:

        db_match = matchRepository.get_match_by_id(match_id)

        if not db_match:
            raise ValueError(
                f"Match with ID {match_id} not found."
            )


        match = MatchResponse(
            id=db_match.id,
            home_team=db_match.home_team,
            away_team=db_match.away_team,
            league=db_match.league,
            match_winner=db_match.match_winner
        )


        prediction = calculate_match_odds(match)


        return match_to_response(
            match,
            prediction
        )