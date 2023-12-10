import pygame

class PacMan(pygame.sprite.Sprite):
    """The pac-man
    """

    def __init__(self):
        super().__init__()
        self.surface = pygame.image.load("assets/pac-man.png").convert()
        self.surface.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surface.get_rect()

    



    
