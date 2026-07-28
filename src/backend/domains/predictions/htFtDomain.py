from dataclasses import dataclass, fields
from typing import Iterable, Any
from util.odds import probability_to_odds


@dataclass
class HtFtProbabilities:
    htft_1_1: float = 0.0
    htft_1_x: float = 0.0
    htft_1_2: float = 0.0

    htft_x_1: float = 0.0
    htft_x_x: float = 0.0
    htft_x_2: float = 0.0

    htft_2_1: float = 0.0
    htft_2_x: float = 0.0
    htft_2_2: float = 0.0

    def to_odds(self )-> "HtFtProbabilities": 
        return HtFtProbabilities(**{field.name: probability_to_odds(getattr(self, field.name)) 
                                    for field in fields(self)})



    
    @classmethod
    def from_db_rows(cls, rows: Iterable[tuple[str, Any, float]]) -> "HtFtProbabilities":

        valid_fields = {field for field in cls.__annotations__}

        data = {}

        for combo, _, probability in rows:
            field = f"htft_{combo.replace('/', '_').lower()}"

            if field in valid_fields:
                data[field] = float(probability)

        return cls(**data)




@dataclass
class MatchHtFtOdds:
    home: HtFtProbabilities
    away: HtFtProbabilities