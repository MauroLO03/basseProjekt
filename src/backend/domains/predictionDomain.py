from pydantic import BaseModel
from domains.predictions.matchWinnerDomain import MatchWinnerPrediction


class Prediction(BaseModel):
    matchWinner: MatchWinnerPrediction