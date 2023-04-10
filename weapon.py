import pygame
from settings import *

class Laser(pygame.sprite.Sprite):
    def __init__(self, position, reverse = False) -> None:
        super().__init__()
        self.image = pygame.Surface((4, 10))
        self.image.fill('red')
        self.rect = self.image.get_rect(center = position)
        if reverse:
            self.speed = -WEAPON_SPEED
        else:
            self.speed = WEAPON_SPEED
        
    def destoy_bullet(self):
        if self.rect.y <= -50 or self.rect.y >= HEIGHT + 50:
            self.kill()
        
    def update(self):
        self.rect.y -= self.speed
        self.destoy_bullet()