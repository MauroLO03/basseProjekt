from dataclasses import dataclass


@dataclass
class xG:
    home_xG: float
    away_xG: float
    match_xG: float