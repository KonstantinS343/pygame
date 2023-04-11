import pygame
from random import choice
import sys

from settings import *
from menu import Menu
from player import Player
from alien import *
from weapon import Laser

temp = ['blue_alien', 'orange_alien', 'pink_alien']

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Space Invanders')
        
        self.menu = Menu(self.screen, [], self)
        self.clock = pygame.time.Clock()
        self.player_sprite = Player((WIDTH//2, HEIGHT), WIDTH, self.screen)
        self.player = pygame.sprite.GroupSingle(self.player_sprite)
        self.aliens = pygame.sprite.Group()
        self.aliens_laser = pygame.sprite.Group()
        self.aliens_setup(2, 2)
        
        self.background = pygame.image.load(PATH_FOR_GAME_BACKGROUND)
        self.run = True
        
    def run_game(self):
       self.menu.start_main_menu() 
       
    def backgroud_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load(SOUND_FOR_GAME_BACKGROUD)
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play()
    
       
    def aliens_setup(self, rows, columns):
        self.aliens.add(ShooterAlien(100, 100, self))
        self.aliens.add(SniperAlien(200, 200, self))
        self.aliens.add(OneShootAlien(400, 100, self))
        self.aliens.add(BossAlien(400, 400, self))
        self.aliens.add(HardAlien(50, 50, self))
        for row_index, row_item in enumerate(range(rows)):
            for columns_index, columns_item in enumerate(range(columns)):
                x = columns_index * 50 + WIDTH//3
                y = row_index * 40 + 200
                alien_sprite = Alien(x, y, self)
                self.aliens.add(alien_sprite)
        self.aliens.add(SpeedAlien(400, 400, self))
    
    def aliens_cheker(self):
        for alien in self.aliens.sprites():
            if alien.rect.right >= WIDTH:
                alien.direction = -ALIENS_SPEED
                for i in self.aliens.sprites():
                    if i.type == alien.type:
                        i.direction = -ALIENS_SPEED
                        self.aliens_move_down(i)
            elif alien.rect.left <= 0:
                alien.direction = ALIENS_SPEED
                for i in self.aliens.sprites():
                    if i.type == alien.type:
                        i.direction = ALIENS_SPEED
                        self.aliens_move_down(i)
    
    def check_destroy(self):
        if self.player.sprite.weapon:
            for laser in self.player.sprite.weapon:
                aliens_hit = pygame.sprite.spritecollide(laser, self.aliens, False)
                if aliens_hit:
                    for i in aliens_hit:
                        self.player_sprite.score += i.score
                        i.hp -= 1
                        if i.hp <= 0:
                            pygame.sprite.spritecollide(laser, self.aliens, True)
                    laser.kill()
                    
        if self.aliens_laser:
            for alien_lasers in self.aliens_laser:
                if pygame.sprite.spritecollide(alien_lasers, self.player, False):
                    alien_lasers.kill()
                    self.player_sprite.lives -= alien_lasers.hp_damage
                    if self.player_sprite.lives <= -10000:
                        pygame.quit()
                        sys.exit()
        
        if self.aliens:
            for alien in self.aliens:
                if pygame.sprite.spritecollide(alien, self.player, False):
                    pygame.quit()
                    sys.exit()
    
    def aliens_shoot(self):
        if self.aliens.sprites():
            random_alien = choice(self.aliens.sprites())
            while random_alien.type == 'orange_alien':
                random_alien = choice(self.aliens.sprites())
            alien_shoot = Laser(random_alien.rect.center, True)
            self.aliens_laser.add(alien_shoot)
    
    def aliens_move_down(self, alien):
        if alien.type == 'white_alien':
            alien.rect.y += ALIENS_SPEED*2
            
         
    def play_game(self):
        ALIENS_SHOOT = pygame.USEREVENT + 1
        pygame.time.set_timer(ALIENS_SHOOT, 600)
        self.backgroud_music()
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == ALIENS_SHOOT:
                    self.aliens_shoot()
            self.clock.tick(60)
            
            self.screen.blit(self.background,(0, 0))
            self.player.sprite.weapon.draw(self.screen)
            self.player.draw(self.screen)
            self.aliens.draw(self.screen)
            self.aliens.update()
            self.aliens_cheker()
            self.aliens_laser.update()
            self.check_destroy()
            self.player_sprite.display_lives()
            self.player_sprite.display_score()
            
            self.player.update()
            self.aliens_laser.draw(self.screen)
            pygame.display.update()
        pygame.quit()
        sys.exit()