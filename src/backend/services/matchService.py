from domains.matchDomain import Match
from repository.matchRepository import matchRepository
from Schemas.match_mapper import match_to_response
from Schemas.matchSchema import MatchResponse
from services.predictionService import PredictionService

class MatchService:

    @staticmethod
    def get_match_by_id(match_id: int) -> MatchResponse:

        match = matchRepository.get_match_by_id(match_id)

        if not match:
            raise ValueError(
                f"Match with ID {match_id} not found."
            )

        print(f"Match info: {match}")


        prediction = PredictionService.calculate_match_odds(match)


        return match_to_response(
            match,
            prediction
        )