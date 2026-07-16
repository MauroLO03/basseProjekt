from pydantic import BaseModel
from typing import List
from schemas.prediction_schema import Prediction


class MatchResponse(BaseModel):
    id: int
    homeTeam: str
    awayTeam: str
    matchWinner: str | None
    league: str
    prediction: Prediction
    