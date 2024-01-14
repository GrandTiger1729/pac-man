from typing import *
from enum import *
import abc

from ..config import *
from .agent import *

class BasePacMan(Agent, metaclass=abc.ABCMeta):
    
    def valid_position(self, position: Position, field: List[List[Square]]) -> None:

        coordinate = position.to_coordinate()
        if field[coordinate.i][coordinate.j] not in [Square.DOT, Square.BIGDOT, Square.EMPTY]:
            return False
        
        return True

class PacManUser(BasePacMan):

    def __init__(self) -> None:

        # super().__init__(Position(14 * CELL_SIZE, 23.5 * CELL_SIZE))
        super().__init__(Position(430.0, 470.0))

class PacManAI(BasePacMan):

    def __init__(self) -> None:

        super().__init__(Position(0, 0))

    def generate_move(ghost_positions: List[Position]) -> Direction:

        pass
