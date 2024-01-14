from typing import *
from enum import *
import random
import sys

import pygame

from ..core import *
from ..config import *

class Environment:

    def __init__(self):
        self.field = Field()
        self.renderer = Renderer()
    
    @classmethod
    def check_quit(cls) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False

    @classmethod
    def get_user_input(cls) -> pygame.key.ScancodeWrapper:

        if cls.check_quit():
            pygame.quit()
            sys.exit()
        
        return pygame.key.get_pressed()

    def play_commands(self, keys: pygame.key.ScancodeWrapper):

        if keys[pygame.K_UP]:
            self.field.pacman_user.move(Direction.UP, self.field.field)
        elif keys[pygame.K_DOWN]:
            self.field.pacman_user.move(Direction.DOWN, self.field.field)
        elif keys[pygame.K_LEFT]:
            self.field.pacman_user.move(Direction.LEFT, self.field.field)
        elif keys[pygame.K_RIGHT]:
            self.field.pacman_user.move(Direction.RIGHT, self.field.field)
        
            print("OK")


    def update(self):
        self.play_commands(self.get_user_input())
        self.renderer.render(self.field)


class Renderer:
    """Show the game status to the screen
    """

    def __init__(self):
        
        pygame.init()
        window_size = (WIDTH, HEIGHT)
        self.screen = pygame.display.set_mode(window_size)
        self.screen.fill((255, 255, 255))
        pygame.display.set_caption('Pac-Man')
        self.clock = pygame.time.Clock()
        pygame.display.update()

    def draw_square(self, i: int, j: int, square: Square):

        match square:
            case Square.EMPTY:
                rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                # pygame.draw.rect(self.screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), rect, 1)
                self.screen.fill((255, 0, 0), rect)
            case Square.DOT:
                rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                # pygame.draw.rect(self.screen, (0, 0, 255), rect, 1)
                self.screen.fill((0, 0, 255), rect)
            case Square.BIGDOT:
                rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                # pygame.draw.rect(self.screen, (0, 255, 0), rect, 1)
                self.screen.fill((0, 255, 0), rect)
            case Square.WALL:
                rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), rect, 1)
            case Square.DOOR:
                rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                self.screen.fill((255, 255, 0), rect)
            case _:
                pass
    
    def draw_field(self, field: List[List[Square]]):
        
        for i in range(FIELD_HEIGHT):
            for j in range(FIELD_WIDTH):
                self.draw_square(i, j, field[i][j])

    def draw_agent(self, agent: Agent):

        (x, y) = agent.position.x, agent.position.y
        pygame.draw.circle(self.screen, (127, 255, 0), (x, y), CELL_SIZE // 2)
        pygame.draw.circle(self.screen, (0, 0, 0), (x, y), CELL_SIZE // 2, 2)

    def render(self, field: Field):

        self.screen.fill((255, 255, 255))
        self.draw_field(field.field)
        self.draw_agent(field.pacman_user)
        print(field.pacman_user.position.x, field.pacman_user.position.y, sep=", ")
        
        pygame.display.update()
        self.clock.tick(FPS)