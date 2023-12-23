from typing import *
from enum import *

from .config import *


class Position:
    """Represent the position where an item currently in.
    """

    __slots__ = (
        "_x",
        "_y",
    )

    def __init__(self, x: int, y: int) -> None:

        # Fit into the board
        self._x: int = max(0, min(x, WIDTH))
        self._y: int = max(0, min(y, HEIGHT))

    @property
    def x(self) -> int:
        return self._x
    
    @x.setter
    def x(self, value) -> None:
        self._x = max(0, min(value, WIDTH))

    @property
    def y(self) -> int:
        return self._y
    
    @y.setter
    def y(self, value) -> None:
        self._y = max(0, min(value, HEIGHT))


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


class Agent:

    __slots__ = (
        "_position",
        "_face",
    )

    def __init__(self, position: Position, face: Face = Face.UP) -> None:
        
        self._position: Position = position
        self._face = face

    @property
    def position(self):
        return self._position
    
    @property
    def face(self):
        return self._face
    
    def move(self, direction: Direction) -> None:
        
        match direction:

            case Direction.UP:
                self._position.y -= 1
                self._face = Face.UP

            case Direction.DOWN:
                self._position.y += 1
                self._face = Face.DOWN

            case Direction.LEFT:
                self._position.x -= 1
                self._face = Face.LEFT

            case Direction.RIGHT:
                self._position.x += 1
                self._face = Face.RIGHT
   
    
    def move_to(self, position: Position) -> None:
        
        self._position = position
