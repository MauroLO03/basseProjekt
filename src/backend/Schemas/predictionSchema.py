from pydantic import BaseModel
from typing import List

class WinnerOdds(BaseModel):
    home: float
    draw: float
    away: float

class HalfTimeFullTimeOdds(BaseModel):
    homeHome: float
    homeDraw: float
    homeAway: float
    drawHome: float
    drawDraw: float
    drawAway: float
    awayHome: float
    awayDraw: float
    awayAway: float

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
    halfTimeFullTime: HalfTimeFullTimeOdds
    goals: GoalsOdds
    corners: CornerOdds
    cards: CardOdds
    bothTeamsScored: BothTeamsScoredOdds