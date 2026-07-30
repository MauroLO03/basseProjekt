from pydantic import BaseModel
from domains.predictions.matchWinnerDomain import MatchWinnerPrediction
from domains.predictions.htFtDomain import MatchHtFtOdds
from domains.predictions.matchOverUnderDomain import MatchOverUnder


class Prediction(BaseModel):
    matchWinner: MatchWinnerPrediction
    htFtOdds: MatchHtFtOdds
    overUnderOdds: MatchOverUnder