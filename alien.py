import pygame
from settings import *
class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.image = pygame.image.load(PATH_FOR_WHITE_ALIEN)
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(topleft = (x, y))