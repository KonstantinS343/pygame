import pygame

from game.config.settings import *
from game.weapon import *

class Player(pygame.sprite.Sprite):
    def __init__(self, position, border_width, screen) -> None:
        super().__init__()
        self.image = pygame.image.load(PATH_FOR_PLAYER).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(midbottom = position)
        self.screen = screen
        self.score = 0
        self.font = pygame.font.Font(SCORE_FONT, 20)
        self.lives = 6
        self.lives_image = pygame.image.load(PATH_FOR_PLAYER).convert_alpha()
        self.lives_image = pygame.transform.scale(self.lives_image, (20, 20))
        self.lives_image_start_draw_x = WIDTH - (self.lives_image.get_size()[0]*5 + 30)
        
        self.border_width = border_width
        self.speed = PLAYER_SPEED
        
        self.ready_for_shoot = True
        self.shoot_time = 0
        self.shoot_cooldown = 1
        self.weapon = pygame.sprite.Group()
        self.player_name = ''
    
    def handle_input(self, wave):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        elif keys[pygame.K_a]:
            self.rect.x -= self.speed
        
        if keys[pygame.K_SPACE] and self.ready_for_shoot:
            self.shoot(wave)
            self.shoot_sound()
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
      
    def display_score(self):
        score_image = self.font.render(f'SCORE: {self.score}', False, 'white')  
        score_rect = score_image.get_rect(topleft = (0, 0))
        self.screen.blit(score_image, score_rect)
        
    def display_lives(self):
        for live in range(self.lives - 1):
            x = self.lives_image_start_draw_x + (live*self.lives_image.get_size()[0] + 20)
            self.screen.blit(self.lives_image, (x, 20))
        
    def shoot(self, wave):
        if wave < 10:
            self.weapon.add(Laser(self.rect.center))
        elif wave >= 10 and wave < 15:
            self.weapon.add(DoubleLaser(self.rect.center))
            self.shoot_cooldown = DoubleLaser(self.rect.center).player_cooldown
        elif wave >= 15:
            self.weapon.add(HighDamageLaser(self.rect.center))
            self.shoot_cooldown = HighDamageLaser(self.rect.center).player_cooldown
        
    def shoot_sound(self):
        pygame.mixer.init()
        pygame.mixer.music.load(SOUND_FOR_SHOOT)
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()

    def update(self, wave):
       self.handle_input(wave) 
       self.border()
       self.recharge()
       self.weapon.update()
       
    
                
