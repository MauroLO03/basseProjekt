from dataclasses import dataclass
from typing import List
from domains.predictions.overUnderDomain import overUnder


@dataclass
class MatchOverUnder:
    overUnder: List[overUnder]