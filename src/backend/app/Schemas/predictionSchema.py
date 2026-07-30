from pydantic import BaseModel
from typing import List

class WinnerOdds(BaseModel):
    home: float
    draw: float
    away: float

class HtFtProbability(BaseModel):
    htft_1_1: float
    htft_1_x: float
    htft_1_2: float

    htft_x_1: float
    htft_x_x: float
    htft_x_2: float

    htft_2_1: float
    htft_2_x: float
    htft_2_2: float


class HalfTimeFullTimeOdds(BaseModel):
    home: HtFtProbability
    away: HtFtProbability    

class GoalLine(BaseModel):
    line: float
    over: float
    under: float

class GoalsOdds(BaseModel):
    overUnder: List[GoalLine]

class CornerLine(BaseModel):
    line: float
    over: float
    under: float

class CornerOdds(BaseModel):
    overUnder: List[CornerLine]

class CardLine(BaseModel):
    line: float
    over: float
    under: float

class CardOdds(BaseModel):
    overUnder: List[CardLine]

class BothTeamsScoredOdds(BaseModel):
    yes: float
    no: float

class PredictionResponse(BaseModel):
    matchWinner: WinnerOdds
    htFtProbabilities: HalfTimeFullTimeOdds