from typing import *
from enum import *

from ..config import *

class Coordinate:
    """Represent the coordinate where an item currently in the field.
    """

    __slots__ = (
        "_i",
        "_j",
    )

    def __init__(self, i: int, j: int) -> None:

        # Fit into the board
        self._i: int = (int(i) + FIELD_HEIGHT) % FIELD_HEIGHT
        self._j: int = (int(j) + FIELD_WIDTH) % FIELD_WIDTH
        
    @property
    def i(self) -> int:
        return self._i
    
    @i.setter
    def i(self, i) -> None:
        self._i = (int(i) + FIELD_HEIGHT) % FIELD_HEIGHT

    @property
    def j(self) -> int:
        return self._j
    
    @j.setter
    def j(self, j) -> None:
        self._j = (int(j) + FIELD_WIDTH) % FIELD_WIDTH

class Position:
    """Represent the absolute coordinate where an item currently in.
    """

    __slots__ = (
        "_x",
        "_y",
    )

    def __init__(self, x: int, y: int) -> None:

        W = FIELD_WIDTH * CELL_SIZE
        H = FIELD_HEIGHT * CELL_SIZE
        self._x: int = (x + W) % W
        self._y: int = (y + H) % H

    @property
    def x(self) -> int:
        return self._x
    
    @x.setter
    def x(self, x) -> None:
        W = FIELD_WIDTH * CELL_SIZE
        self._x = (x + W) % W

    @property
    def y(self) -> int:
        return self._y
    
    @y.setter
    def y(self, y) -> None:
        H = FIELD_HEIGHT * CELL_SIZE
        self._y = (y + H) % H

    def to_coordinate(self) -> Coordinate:
        return Coordinate(self.y // CELL_SIZE, self.x // CELL_SIZE)


class Face(Enum):

    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()

class Direction(Enum):

    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()

class Square(Enum):

    EMPTY = auto()
    WALL = auto()
    BIGDOT = auto()
    DOT = auto()
    DOOR = auto()
    BOX = auto()

class Event(Enum):

    NORMAL = auto()
    REVERSED = auto()