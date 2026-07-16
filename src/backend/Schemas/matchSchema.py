from pydantic import BaseModel
from typing import List
from Schemas.predictionSchema import PredictionResponse


class MatchResponse(BaseModel):
    id: int
    homeTeam: str
    awayTeam: str
    matchWinner: str | None
    league: str
    prediction: PredictionResponse 
    