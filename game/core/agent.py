from typing import *
from enum import *

from .types import *
from ..config import *

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
    
    def valid_position(self, position: Position, field: List[List[Square]]) -> bool:
        
        raise NotImplementedError
    
    def check_valid(self, position: Position, field: List[List[Square]]) -> bool:
        """Check whether the edge of the agent is in a valid cell"""
        EPS = 1e-6
        return self.valid_position(Position(position.x, position.y - CELL_SIZE // 2 + EPS), field) and \
               self.valid_position(Position(position.x, position.y + CELL_SIZE // 2 - EPS), field) and \
               self.valid_position(Position(position.x - CELL_SIZE // 2 + EPS, position.y), field) and \
               self.valid_position(Position(position.x + CELL_SIZE // 2 - EPS, position.y), field)
    
    def move(self, direction: Direction, field: List[List[Square]]) -> None:
        
        match direction:

            case Direction.UP:
                new_position = Position(self.position.x, self.position.y - VELOCITY)
                if self.check_valid(new_position, field):
                    self._position = new_position
                    self._face = Face.UP

            case Direction.DOWN:
                new_position = Position(self.position.x, self.position.y + VELOCITY)
                if self.check_valid(new_position, field):
                    self._position = new_position
                    self._face = Face.DOWN

            case Direction.LEFT:
                new_position = Position(self.position.x - VELOCITY, self.position.y)
                if self.check_valid(new_position, field):
                    self._position = new_position
                    self._face = Face.LEFT

            case Direction.RIGHT:
                new_position = Position(self.position.x + VELOCITY, self.position.y)
                if self.check_valid(new_position, field):
                    self._position = new_position
                    self._face = Face.RIGHT

            case _:
                pass

   
    def move_to(self, position: Position, field: List[List[Square]]) -> None:
        
        assert self.valid_position(position, field)
        self._position = position
