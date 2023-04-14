import json

from game.config.settings import PATH_FOR_TABLE

class Table:
    def __init__(self) -> None:
        self.list_of_player = dict()
        self.load_table()
    
    def load_table(self):
        with open(PATH_FOR_TABLE, 'r') as file:
            self.list_of_player = json.load(file)
    
    def upload_table(self):
        with open(PATH_FOR_TABLE, 'w') as file:
            json.dump(self.list_of_player,file,ensure_ascii=False, indent=4)
    
    def create_table_line(self, player_name, score):
        if not player_name:
            player_name = 'Anonymous'
        self.list_of_player[player_name] = score