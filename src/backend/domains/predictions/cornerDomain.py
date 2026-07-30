from dataclasses import dataclass


@dataclass
class CornerDomain:
    line: float
    over: float
    under: float