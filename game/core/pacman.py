from typing import *
from enum import *

from .config import *
from .agent import *

class BasePacMan(Agent):
    pass

class PacManUser(BasePacMan):

    def __init__(self) -> None:

        super().__init__(Position(0, 0))

class PacManAI(BasePacMan):

    def __init__(self) -> None:

        super().__init__(Position(0, 0))

    def generate_move(ghost_positions: List[Position]) -> Direction:

        pass
