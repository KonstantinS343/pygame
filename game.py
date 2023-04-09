import pygame
from settings import *
from menu import Menu
from player import Player
from alien import Alien

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Space Invanders')
        
        self.menu = Menu(self.screen, [], self)
        self.clock = pygame.time.Clock()
        self.player_sprite = Player((WIDTH//2, HEIGHT), WIDTH)
        self.player = pygame.sprite.GroupSingle(self.player_sprite)
        self.aliens = pygame.sprite.Group()
        self.aliens_setup(6, 6)
        
        self.background = pygame.image.load(PATH_FOR_GAME_BACKGROUND)
        self.run = True
        
    def run_game(self):
       self.menu.start_main_menu() 
       
    def aliens_setup(self, rows, columns):
        for row_index, row_item in enumerate(range(rows)):
            for columns_index, columns_item in enumerate(range(columns)):
                x = columns_index * 50 + 100
                y = row_index * 40 + 60
                alien_sprite = Alien(x, y)
                self.aliens.add(alien_sprite)
         
    def play_game(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            self.clock.tick(60)
            
            self.screen.blit(self.background,(0, 0))
            self.player.sprite.weapon.draw(self.screen)
            self.player.draw(self.screen)
            self.aliens.draw(self.screen )
            
            self.player.update()
            pygame.display.update()
        pygame.quit()