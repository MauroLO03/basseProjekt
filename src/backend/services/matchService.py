from pprint import pprint
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



        prediction = PredictionService.calculate_match_odds(match)


        prediction = PredictionService.calculate_match_odds(match)


        print("\n" + "=" * 50)
        print(f" MATCH DATA [ID: {match_id}]")
        print("=" * 50)
        pprint(vars(match) if hasattr(match, "__dict__") else match)

        print("\n" + "-" * 50)
        print(" PREDICTION ODDS")
        print("-" * 50)
        pprint(vars(prediction) if hasattr(prediction, "__dict__") else prediction)
        print("=" * 50 + "\n")

        return match_to_response(
            match,
            prediction
        )