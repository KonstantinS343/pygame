import pygame

from game.config.settings import *

class Laser(pygame.sprite.Sprite):
    def __init__(self, position, reverse = False, speed = False) -> None:
        super().__init__()
        self.image = pygame.Surface((4, 10))
        self.image.fill('red')
        self.hp_damage = 1
        self.player_cooldown = 600
        self.rect = self.image.get_rect(center = position)
        if not speed:
            speed = WEAPON_SPEED

        if reverse:
            self.speed = -speed
        else:
            self.speed = speed
    
    def destroy(self):
        self.kill()
        
    def destoy_bullet(self):
        if self.rect.y <= -50 or self.rect.y >= HEIGHT + 50:
            self.kill()
        
    def update(self):
        self.rect.y -= self.speed
        self.destoy_bullet()

class LaserComboDamage(pygame.sprite.Sprite):
    def __init__(self, position, reverse = False) -> None:
        super().__init__()
        self.image = pygame.Surface((5, 25))
        self.image.fill('white')
        self.hp_damage = 2
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

class OneShootLaser(pygame.sprite.Sprite):
    def __init__(self, position, reverse = False) -> None:
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill('purple')
        self.hp_damage = 10
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
        
class DoubleLaser(pygame.sprite.Sprite):
    def __init__(self, position, reverse = False, speed = False) -> None:
        super().__init__()
        self.image = pygame.Surface((4, 15))
        self.image.fill('green')
        self.hp_damage = 1
        self.player_cooldown = 1
        self.rect = self.image.get_rect(center = position)
        
        if not speed:
            speed = WEAPON_SPEED + 1

        if reverse:
            self.speed = -speed
        else:
            self.speed = speed + 1
        
    def destoy_bullet(self):
        if self.rect.y <= -50 or self.rect.y >= HEIGHT + 50:
            self.kill()
    
    def destroy(self):
        self.kill()
        
    def update(self):
        self.rect.y -= self.speed
        self.destoy_bullet()
        
class HighDamageLaser(pygame.sprite.Sprite):
    def __init__(self, position, reverse = False, speed = False) -> None:
        super().__init__()
        self.image = pygame.Surface((4, 15))
        self.image.fill('blue')
        self.hp_damage = 2
        self.player_cooldown = 1
        self.rect = self.image.get_rect(center = position)
        
        if not speed:
            speed = WEAPON_SPEED + 1

        if reverse:
            self.speed = -speed
        else:
            self.speed = speed + 1
        
    def destoy_bullet(self):
        if self.rect.y <= -50 or self.rect.y >= HEIGHT + 50:
            self.kill()
    
    def destroy(self):
        self.kill()
        
    def update(self):
        self.rect.y -= self.speed
        self.destoy_bullet()

