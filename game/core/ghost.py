from typing import *
from enum import *
import abc

from .config import *
from .agent import *

class BaseGhost(Agent, metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def generate_move(pacman_positions: List[Position]) -> Direction:

        raise NotImplementedError

class Blinky(BaseGhost):

    def __init__(self) -> None:

        super().__init__(Position(0, 0))

    def generate_move(pacman_positions: List[Position]) -> Direction:

        pass

class Inky(BaseGhost):

    def __init__(self) -> None:

        super().__init__(Position(0, 0))

    def generate_move(pacman_positions: List[Position]) -> Direction:

        pass
    
class Pinky(BaseGhost):

    def __init__(self) -> None:

        super().__init__(Position(0, 0))

    def generate_move(pacman_positions: List[Position]) -> Direction:

        pass
    

class Clyde(BaseGhost):

    def __init__(self) -> None:

        super().__init__(Position(0, 0))

    def generate_move(pacman_positions: List[Position]) -> Direction:

        pass
