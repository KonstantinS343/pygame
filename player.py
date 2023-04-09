import pygame

from settings import *
from weapon import Laser

class Player(pygame.sprite.Sprite):
    def __init__(self, position, border_width) -> None:
        super().__init__()
        self.image = pygame.image.load(PATH_FOR_PLAYER).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(midbottom = position)
        
        self.border_width = border_width
        self.speed = PLAYER_SPEED
        
        self.ready_for_shoot = True
        self.shoot_time = 0
        self.shoot_cooldown = 600
        self.weapon = pygame.sprite.Group()
    
    def handle_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        elif keys[pygame.K_a]:
            self.rect.x -= self.speed
        
        if keys[pygame.K_SPACE] and self.ready_for_shoot:
            self.shoot()
            self.ready_for_shoot = False
            self.shoot_time = pygame.time.get_ticks()
            
    def recharge(self):
        if not self.ready_for_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time >= self.shoot_cooldown:
                self.ready_for_shoot = True
            
    def border(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.left >= self.border_width-40:
            self.rect.left = self.border_width-40  
        
    def shoot(self):
        self.weapon.add(Laser(self.rect.center))      
    
    def update(self):
       self.handle_input() 
       self.border()
       self.recharge()
       self.weapon.update()
       
    
                
