from pydantic import BaseModel
from typing import List
from Schemas.predictionSchema import PredictionResponse


class MatchResponse(BaseModel):
    id: int
    homeTeamId: int
    awayTeamId: int
    leagueId: int
    date: str
    prediction: PredictionResponse 
    