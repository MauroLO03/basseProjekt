from dataclasses import dataclass
from typing import List
from domains.predictions.cornerDomain import CornerDomain


@dataclass
class MatchCornerDomain:
    overUnder: List[CornerDomain]