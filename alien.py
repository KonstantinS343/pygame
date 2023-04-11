import pygame
from weapon import *

from settings import *

class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y, game_object) -> None:
        super().__init__()
        self.type = 'white_alien'
        self.score = 1
        self.game = game_object
        self.image = pygame.image.load(PATH_FOR_WHITE_ALIEN)
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(topleft = (x, y))
        
    def update(self, aliens_direction):
        self.rect.x += aliens_direction
        
class ShooterAlien(pygame.sprite.Sprite):
    def __init__(self, x, y, game_object) -> None:
        super().__init__()
        self.type = 'orange_alien'
        self.game = game_object
        self.score = 5
        self.image = pygame.image.load(PATH_FOR_ORANGE_ALIEN)
        self.shoot_cooldown = 1000
        self.ready_shoot = True
        self.shoot_time = 0
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(topleft = (x, y))
        
    def update(self, aliens_direction):
        alien_shoot = LaserComboDamage(self.rect.center, True)
        if self.ready_shoot:
            self.game.aliens_laser.add(alien_shoot)
            self.ready_shoot = False
            self.shoot_time = pygame.time.get_ticks()
        self.recharge()
    
    def recharge(self):
        if not self.ready_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time >= self.shoot_cooldown:
                self.ready_shoot = True

class SpeedAlien(pygame.sprite.Sprite):
    def __init__(self, x, y, game_object) -> None:
        super().__init__()
        self.type = 'blue_alien'
        self.score = 3
        self.game = game_object
        self.image = pygame.image.load(PATH_FOR_BLUE_ALIEN)
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(topleft = (x, y))
        
    def update(self, aliens_direction):
        self.rect.x += aliens_direction*3
    
class OneShootAlien(pygame.sprite.Sprite):
    def __init__(self, x, y, game_object) -> None:
        super().__init__()
        self.type = 'pink_alien'
        self.score = 10
        self.game = game_object
        self.image = pygame.image.load(PATH_FOR_PINK_ALIEN)
        self.shoot_cooldown = 2000
        self.ready_shoot = True
        self.shoot_time = 0
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(topleft = (x, y))
        
    def update(self, aliens_direction):
        alien_shoot = OneShootLaser(self.rect.center, True)
        if self.ready_shoot:
            self.game.aliens_laser.add(alien_shoot)
            self.ready_shoot = False
            self.shoot_time = pygame.time.get_ticks()
        self.recharge()
    
    def recharge(self):
        if not self.ready_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time >= self.shoot_cooldown:
                self.ready_shoot = True
                
class SniperAlien(pygame.sprite.Sprite):
    def __init__(self, x, y, game_object) -> None:
        super().__init__()
        self.type = 'red_alien'
        self.score = 8
        self.game = game_object
        self.image = pygame.image.load(PATH_FOR_RED_ALIEN)
        self.shoot_cooldown = 3000
        self.ready_shoot = True
        self.shoot_time = 0
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(topleft = (x, y))
        
    def update(self, aliens_direction):
        alien_shoot = Laser(self.rect.center, True, 12)
        if self.ready_shoot:
            self.game.aliens_laser.add(alien_shoot)
            self.ready_shoot = False
            self.shoot_time = pygame.time.get_ticks()
        self.recharge()
    
    def recharge(self):
        if not self.ready_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time >= self.shoot_cooldown:
                self.ready_shoot = True