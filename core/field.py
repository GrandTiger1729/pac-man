from enum import *

import pygame

from .config import *


class Square(Enum):

    EMPTY = auto()
    PACMAN = auto()
    GHOST = auto()

class Field:

    def __init__(self):

        self.reset()


    def reset(self):

        self.field = STANDARD_FIELD


    