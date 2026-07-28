from pydantic import BaseModel
from domains.predictions.matchWinnerDomain import MatchWinnerPrediction
from domains.predictions.htFtDomain import MatchHtFtOdds


class Prediction(BaseModel):
    matchWinner: MatchWinnerPrediction
    htFtOdds: MatchHtFtOdds