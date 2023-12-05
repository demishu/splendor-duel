from collections.abc import Iterable
from pathlib import Path
from .gems import Gems
from .effects import Effect
from typing import Type

color = Type[str]


class Card:
    id: int
    color: color
    tier: int
    costs: dict[color: int]
    effect: Effect = None
    victory_points: int
    pic: Path


