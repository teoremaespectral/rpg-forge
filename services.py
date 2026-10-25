from domain import Stat, Character, User, Board
from random import randint
import setup
import re

class RollEngine:
    '''Class responsible for parsing roll commands and executing rolls.'''

    @staticmethod
    def roll(num_dice: int = 1, num_sides: int = 20):
        rolls = [randint(1, num_sides) for _ in range(num_dice)]
        return sum(rolls), rolls

    @staticmethod
    def parse_roll_command(command: str):
        regex = r"((?P<qtd>\d+)d(?P<lados>\d+) *)((?P<modificador>[+-]\d+) *)?"
        match = re.match(regex, command.lower())
        
        if not match:
            raise ValueError("Invalid roll command format.")
        
        num_dice = int(match.group("qtd")) if match.group("qtd") else 1
        num_sides = int(match.group("lados")) if match.group("lados") else 20
        modifier = int(match.group("modificador")) if match.group("modificador") else 0
        
        return num_dice, num_sides, modifier

    @staticmethod
    def execute_roll(command: str):
        num_dice, num_sides, modifier = RollEngine.parse_roll_command(command)
        total, rolls = RollEngine.roll(num_dice, num_sides)
        total += modifier
        return {
            "rolls": rolls,
            "modifier": modifier,
            "total": total
        }


class Manager:
    def __init__(self):
        self.STATS = setup.STATS
        self.CHARACTERS = setup.CHARACTERS
        self.USERS = setup.USERS
        self.BOARD = setup.BOARD

        self.board = self.make_board()

    def make_board(self):
        characters = []
        for char_name, char_data in self.CHARACTERS.items():
            stats = []
            for stat_name, stat_value in char_data["stats"].items():
                stat_info = self.STATS[stat_name]
                stat = Stat(name=stat_info["name"], value=stat_value)
                stats.append(stat)
            character = Character(name=char_name, stats=stats)
            characters.append(character)

        users = []
        for user_name, user_data in self.USERS.items():
            user_characters = [char for char in characters if char.name in user_data["characters"]]
            user = User(username=user_name, user_id=user_data["user_id"], is_gm=user_data["is_gm"], characters=user_characters)
            users.append(user)

        board = Board(name=self.BOARD["name"], board_id=self.BOARD["board_id"], users=users)
        return board