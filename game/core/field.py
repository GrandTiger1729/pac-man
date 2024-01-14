from typing import *
from enum import *

from ..config import *
from .types import *
from .pacman import PacManUser, PacManAI
from .ghost import Blinky, Inky, Pinky, Clyde

class Field:

    __slots__ = (
        "_field",
        "_event",
        "_live_count",
        "_fruits",
        "_score",
        "_pacman_user",
        "_pacman_ai",
        "_blinky",
        "_inky",
        "_pinky",
        "_clyde",
    )

    def __init__(self):

        self.reset()

    @property
    def field(self) -> List[List[Square]]:
        return self._field
    
    @property
    def event(self) -> Event:
        return self._event
    
    @property
    def live_count(self) -> int:
        return self._live_count
    
    @property
    def score(self) -> int:
        return self._score
    
    @property
    def pacman_user(self) -> PacManUser:
        return self._pacman_user
    
    @property
    def pacman_ai(self) -> PacManAI:
        return self._pacman_ai
    
    @property
    def blinky(self) -> Blinky:
        return self._blinky
    
    @property
    def inky(self) -> Inky:
        return self._inky
    
    @property
    def pinky(self) -> Pinky:
        return self._pinky
    
    @property
    def clyde(self) -> Clyde:
        return self._clyde
    

    def reset(self):

        # build left half side of the field
        self._field = [
        #                0,             1,             2,             3,             4,             5,             6,             7,             8,             9,            10,            11,            12,            13,
            [Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL],
            [Square.  WALL, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.  WALL],
            [Square.  WALL, Square.   DOT, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL],
            [Square.  WALL, Square.BIGDOT, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL],
            [Square.  WALL, Square.   DOT, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL],
            [Square.  WALL, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT],
            [Square.  WALL, Square.   DOT, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL],
            [Square.  WALL, Square.   DOT, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL],
            [Square.  WALL, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.  WALL, Square.  WALL, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.  WALL],
            [Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL],
            [Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL],
            [Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL, Square.  WALL, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT],
            [Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL, Square.  WALL, Square.  WALL, Square.  DOOR],
            [Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL, Square.   BOX, Square.   BOX, Square.   BOX],
            [Square. EMPTY, Square. EMPTY, Square. EMPTY, Square. EMPTY, Square. EMPTY, Square. EMPTY, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.  WALL, Square.   BOX, Square.   BOX, Square.   BOX], # midpoint
            [Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL, Square.   BOX, Square.   BOX, Square.   BOX],
            [Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL],
            [Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL, Square.  WALL, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT],
            [Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL],
            [Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL],
            [Square.  WALL, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.  WALL],
            [Square.  WALL, Square.   DOT, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL],
            [Square.  WALL, Square.BIGDOT, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL],
            [Square.  WALL, Square.   DOT, Square.   DOT, Square.   DOT, Square.  WALL, Square.  WALL, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT],
            [Square.  WALL, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL],
            [Square.  WALL, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL],
            [Square.  WALL, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.  WALL, Square.  WALL, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.  WALL],
            [Square.  WALL, Square.   DOT, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL],
            [Square.  WALL, Square.   DOT, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.   DOT, Square.  WALL],
            [Square.  WALL, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT, Square.   DOT],
            [Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL, Square.  WALL],
        ]

        # extend to the right hand side because it is bilateral symmetry
        for i in range(FIELD_HEIGHT):
            self._field[i].extend(reversed(self._field[i]))

        self._event = Event.NORMAL
        self._live_count = LIVE_COUNT
        self._score = 0
        self._pacman_user = PacManUser()
        self._pacman_ai = PacManAI()
        self._blinky = Blinky()
        self._inky = Inky()
        self._pinky = Pinky()
        self._clyde = Clyde()

    def _check_collisions(self) -> bool:

        pass

    def update(self):

        pass

    def is_gameover(self):

        pass

    