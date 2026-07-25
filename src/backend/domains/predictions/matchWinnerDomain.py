from dataclasses import dataclass


@dataclass
class MatchWinnerPrediction:
    home: float
    draw: float
    away: float