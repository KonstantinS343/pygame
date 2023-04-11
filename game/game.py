import pygame
from random import choice
import sys
import json
import time

from game.settings import *
from game.menu import Menu
from game.player import Player
from game.alien import *
from game.weapon import Laser

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
        
        self.background = pygame.image.load(PATH_FOR_GAME_BACKGROUND)
        self.run = True
        self.wave = 0
        self.font = pygame.font.Font(SCORE_FONT, 20)
        
    def run_game(self):
       self.menu.start_main_menu() 
       
    def backgroud_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load(SOUND_FOR_GAME_BACKGROUD)
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play()
    
       
    def aliens_setup(self):
        with open('game/waves_controller.json', 'r') as file:
            aliens = json.load(file)
        for i in aliens[0]['Wave1']:
            self.aliens.add(Alien(i[1], i[2], self))
    
    def aliens_cheker(self):
        for alien in self.aliens.sprites():
            if alien.rect.right >= WIDTH:
                alien.direction = -alien.direction if alien.direction > 0 else alien.direction
                for i in self.aliens.sprites():
                    if i.type == alien.type:
                        i.direction = -alien.direction if alien.direction > 0 else alien.direction
                        self.aliens_move_down(i)
            elif alien.rect.left <= 0:
                alien.direction = abs(alien.direction)
                for i in self.aliens.sprites():
                    if i.type == alien.type:
                        i.direction = abs(alien.direction)
                        self.aliens_move_down(i)
    
    def check_destroy(self):
        if self.player.sprite.weapon:
            for laser in self.player.sprite.weapon:
                aliens_hit = pygame.sprite.spritecollide(laser, self.aliens, False)
                if aliens_hit:
                    for i in aliens_hit:
                        i.hp -= laser.hp_damage
                        if i.hp <= 0:
                            self.player_sprite.score += i.score
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
        alien = False
        if self.aliens.sprites():
            random_alien = choice(self.aliens.sprites())
            for i in self.aliens.sprites():
                if i.type == 'white_alien' or i.type == 'purple_alien':
                    alien = True
            if alien:
                while random_alien.type != 'white_alien' and random_alien.type != 'purple_alien':
                    random_alien = choice(self.aliens.sprites())
                alien_shoot = Laser(random_alien.rect.center, True)
                self.aliens_laser.add(alien_shoot)
    
    def aliens_move_down(self, alien):
        if alien.type == 'white_alien' or alien.type == 'blue_alien' or \
            alien.type == 'purple_alien' or alien.type == 'dark_blue_alien':
            alien.rect.y += ALIENS_SPEED*3
            
    def waves(self):
        if not self.aliens:
            self.wave += 1
            self.aliens_setup()
            for i in self.aliens_laser:
                i.kill()
            for i in self.player_sprite.weapon:
                i.kill()
            
    def display_waves(self):
        number_waves = self.font.render(f'WAVE {self.wave}', False, 'white')
        waves_rect = number_waves.get_rect(topleft = (200, 0))
        self.screen.blit(number_waves, waves_rect)
         
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
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                         self.waves()
            self.clock.tick(FPS)
            
            self.screen.blit(self.background,(0, 0))
            self.player.sprite.weapon.draw(self.screen)
            self.player.draw(self.screen)
            
            self.display_waves
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