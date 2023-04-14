import pygame_menu
from typing import *

from game.config.settings import *
from game.config.table_records import Table

class Menu:
    def __init__(self, screen, table_od_records, game_object) -> None:
        self.font = pygame_menu.font.FONT_8BIT
        self.game = game_object
        self.screen = screen
        self.table = Table()
        self.create_custom_theme()
        self.create_menu_sound()
        self.change_menu_item_sound()
        self.delete_later_table_od_records: List[Dict[str,object]] = table_od_records
         
        self.menu =  pygame_menu.Menu('Space Invanders',
                                      WIDTH,
                                      HEIGHT,
                                      theme = self.custom_theme
                                      )
        
        self.menu.add.button('Play', self.play)
        self.menu.add.button('Table of records', self.start_table_of_records_menu)
        self.menu.add.button('Help', self.start_help_menu)
        self.menu.add.button('Quit',  pygame_menu.events.EXIT)
        
        self.menu.set_sound(self.menu_sound, recursive=True)
        self.menu.set_sound(self.click_other_menu_sound)
        
    def create_custom_theme(self):
        self.custom_theme = pygame_menu.themes.THEME_DARK.copy()
        self.background_image = pygame_menu.baseimage.BaseImage(
            image_path = PATH_FOR_MENU_BACKGROUND,
            )
        self.custom_theme.background_color = self.background_image
        self.custom_theme.widget_font = self.font
        self.custom_theme.widget_font_size = 30 
        self.custom_theme.widget_padding = (20, 0, 20, 10)
        self.custom_theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY_DIAGONAL
    
    def create_them_for_other_window(self, **kwargs):
        self.other_theme = self.custom_theme.copy()
        if not kwargs:
            self.other_theme.widget_font_size = 30
            self.other_theme.widget_font = pygame_menu.font.FONT_MUNRO
        else:
            self.other_theme.widget_font_size = kwargs['font_size']
            self.other_theme.widget_font = kwargs['font']
        self.other_theme.widget_padding = (0, 0, 0, 0)
        self.other_theme.widget_font_color = (255, 255, 255)
        
    def change_menu_item_sound(self):
        self.click_other_menu_sound = pygame_menu.sound.Sound()
        self.click_other_menu_sound.set_sound(pygame_menu.sound.SOUND_TYPE_WIDGET_SELECTION,
                                            SOUND_FOR_CHANGE_ITEM_IN_MENU)
        
    
    def create_menu_sound(self):
        self.menu_sound = pygame_menu.sound.Sound()
        self.menu_sound.set_sound(pygame_menu.sound.SOUND_TYPE_OPEN_MENU,
            SOUND_FOR_MAIN_MENU
        )
        self.menu_sound.play_open_menu()
    
    def play(self):
        self.menu_sound.pause()
        self.menu_close()
        self.game.play_game()
        
    def table_of_records(self):
        self.table.load_table()
        self.create_them_for_other_window(font_size = 50, font = pygame_menu.font.FONT_MUNRO)
        self.table_scores = pygame_menu.Menu('Table of records',
                                           WIDTH,
                                           HEIGHT,
                                           theme = self.other_theme
                                           )
        for i in self.table.list_of_player.items():
            self.table_scores.add.label(f"{i[0]} : {i[1]} points",
                                        margin = (10, 10))
        self.table_scores.add.button('Back', self.start_main_menu)
        
    def help_menu(self):
       self.create_them_for_other_window()
       self.help_window = pygame_menu.Menu('Help',
                                           WIDTH,
                                           HEIGHT,
                                           theme = self.other_theme
                                           )
       self.help_window.add.label(HELP_TEXT)
       self.help_window.add.button('Back', self.start_main_menu)
       
    def start_help_menu(self):
        self.help_menu()
        self.help_window.mainloop(self.screen)
        
    def start_table_of_records_menu(self):
        self.table_of_records()
        self.table_scores.mainloop(self.screen)
        
    def quit(self):
        pygame_menu.event.EXIT

    def start_main_menu(self):
        self.menu.mainloop(self.screen)
    
    def menu_close(self):
        self.menu.disable()
        
        
