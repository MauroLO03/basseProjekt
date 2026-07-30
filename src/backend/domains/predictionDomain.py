from pydantic import BaseModel
from domains.predictions.matchWinnerDomain import MatchWinnerPrediction
from domains.predictions.htFtDomain import MatchHtFtOdds
from domains.predictions.matchOverUnderDomain import MatchOverUnder
from domains.predictions.matchCornerDomain import MatchCornerDomain
from domains.predictions.matchYellowDomain import MatchYellowDomain


class Prediction(BaseModel):
    matchWinner: MatchWinnerPrediction
    htFtOdds: MatchHtFtOdds
    overUnderOdds: MatchOverUnder
    cornerOdds: MatchCornerDomain
    yellowCardOdds: MatchYellowDomain