from dataclasses import dataclass
from typing import List
from domains.predictions.cardDomain import CardDomain


@dataclass
class MatchYellowDomain:
    overUnder: List[CardDomain]